"""End-to-end test of the offline-first Tour Money PWA using Chromium with mobile dimensions.
Run: python tests/browser_e2e.py (requires playwright and chromium).
No internet is needed: serves the local app on loopback.
"""
import os
import re
import json
import time
import socket
import tempfile
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass

os.chdir(ROOT)
server=ThreadingHTTPServer(('127.0.0.1',0), Quiet)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
url=f'http://127.0.0.1:{server.server_port}/'
errors=[]
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
    ctx=browser.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True,accept_downloads=True)
    pg=ctx.new_page()
    pg.on('pageerror',lambda err:errors.append(str(err)))
    pg.goto(url)
    pg.get_by_text('Financial overview').wait_for(timeout=15000)
    assert pg.get_by_text('Start here: add your total collected tour fund.').count()==1
    pg.get_by_role('button',name='Set initial fund').first.click()
    assert pg.locator('#fund-type').input_value()=='initial'
    pg.locator('#fund-amount').fill('50000')
    pg.locator('#fund-title').fill('Initial fund from participants')
    pg.locator('#fund-form button[type="submit"]').click()
    pg.locator('.hero-balance').get_by_text('৳50,000').wait_for()
    pg.get_by_role('button',name='Add Expense').first.click()
    pg.locator('#ex-title').fill('Lunch')
    pg.locator('#ex-amount').fill('3500.50')
    pg.locator('#ex-cat').select_option(label='Food & Drinks')
    pg.locator('#expense-form button[type="submit"]').click()
    pg.locator('.hero-balance').get_by_text('৳46,499.5').wait_for()
    pg.get_by_role('button',name='Expenses',exact=True).click()
    assert pg.get_by_text('Lunch',exact=True).count()==1
    pg.locator('[data-edit-record]').first.click()
    pg.locator('#ex-amount').fill('4000.50')
    pg.locator('#expense-form button[type="submit"]').click()
    pg.get_by_role('button',name='Home',exact=True).click()
    pg.locator('.hero-balance').get_by_text('৳45,999.5').wait_for()
    pg.get_by_role('button',name='Reports',exact=True).click()
    assert pg.get_by_text('Financial reports').count()==1
    with pg.expect_download() as download_csv:pg.get_by_role('button',name=re.compile('Export CSV')).click()
    csv=Path(download_csv.value.path()).read_text(encoding='utf-8-sig')
    assert 'Lunch' in csv and '4000.50' in csv and 'Initial fund from participants' in csv
    with pg.expect_download() as download_pdf:pg.get_by_role('button',name=re.compile('Export PDF')).click()
    pdf=Path(download_pdf.value.path()).read_bytes()
    assert pdf.startswith(b'%PDF-') and len(pdf)>1000
    pg.get_by_role('button',name='Settings',exact=True).click()
    with pg.expect_download() as download_backup:pg.get_by_role('button',name='Export backup').click()
    raw=Path(download_backup.value.path()).read_bytes()
    backup=json.loads(raw)
    assert backup['format']=='tour-money-backup-v1' and len(backup['state']['transactions'])==2
    assert len(backup['state']['audit'])>=3
    with pg.expect_download() as download_snapshot:pg.get_by_role('button',name='Share viewer snapshot').click()
    snap=Path(download_snapshot.value.path()).read_bytes()
    viewer_path=Path(tempfile.gettempdir())/'tour-money-viewer-test.json'
    viewer_path.write_bytes(snap)
    pg.reload()
    assert pg.get_by_text('Settings',exact=True).count()>=1
    pg.get_by_role('button',name='Home',exact=True).click()
    pg.locator('.hero-balance').get_by_text('৳45,999.5').wait_for()
    # PWA service worker must cache the app so the shell reopens offline.
    pg.wait_for_function('navigator.serviceWorker.controller !== null',timeout=10000)
    ctx.set_offline(True)
    pg.reload(wait_until='load')
    pg.get_by_text('Financial overview').wait_for(timeout=15000)
    assert '৳45,999.5' in pg.locator('.hero-balance').inner_text()
    ctx.set_offline(False)
    pg.screenshot(path='/mnt/data/tour-money-app/dashboard-mobile.png',full_page=True)
    # verify importing snapshot into a different installation (separate browser context) is read-only
    viewer_ctx=browser.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,accept_downloads=True)
    viewer_pg=viewer_ctx.new_page()
    viewer_pg.on('dialog',lambda d:d.accept())
    viewer_pg.goto(url)
    viewer_pg.get_by_role('button',name='Settings',exact=True).click()
    viewer_pg.get_by_role('button',name='Import viewer snapshot').click()
    viewer_pg.locator('#import-file').set_input_files(str(viewer_path))
    viewer_pg.get_by_text('View-only copy').wait_for(timeout=10000)
    assert '৳45,999.5' in viewer_pg.locator('.hero-balance').inner_text()
    assert viewer_pg.locator('button.floating').count()==0
    viewer_pg.reload()
    viewer_pg.get_by_text('View-only copy').wait_for()
    assert not errors,errors
    viewer_ctx.close()
    ctx.close();browser.close()
server.shutdown()
print('PASS: Mobile UI, fund + expense, editing, currency precision, CSV/PDF, JSON backup, offline reload, separate viewer snapshot, IndexedDB persistence')
print('Saved mobile screenshot: /mnt/data/tour-money-app/dashboard-mobile.png')
