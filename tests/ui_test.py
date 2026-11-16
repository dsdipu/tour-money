"""Exercise mobile user interactions in a Chromium DOM under restricted browser policies.
This deliberately bypasses HTTP, IndexedDB, and SW and mocks persistence; these require device testing.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).resolve().parents[1]
s=(p/'app.js').read_text()
assert 'startup();\n})();' in s
s=s.replace('startup();\n})();', 'state=emptyState();storeValues=async()=>{};render();\n})();')
with sync_playwright() as browser_lib:
 browser=browser_lib.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True,accept_downloads=True)
 errors=[]
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body><div id="app"></div><div id="overlay-root"></div><div id="toast-root"></div></body></html>')
 page.add_style_tag(content=(p/'styles.css').read_text())
 page.add_script_tag(content=s)
 page.get_by_text('Financial overview').wait_for()
 page.get_by_role('button',name='Set initial fund').first.click()
 page.locator('#fund-title').fill('Tour collection')
 page.locator('#fund-amount').fill('50000')
 page.locator('#fund-form button[type="submit"]').click()
 page.locator('.hero-balance').get_by_text('৳50,000').wait_for()
 page.get_by_role('button',name='Add Expense').first.click()
 page.locator('#ex-title').fill('Lunch')
 page.locator('#ex-amount').fill('3500.50')
 page.locator('#ex-cat').select_option(label='Food & Drinks')
 page.locator('#expense-form button[type="submit"]').click()
 page.locator('.hero-balance').get_by_text('৳46,499.5').wait_for()
 page.screenshot(path='/mnt/data/tour-money-preview.png',full_page=True)
 page.get_by_role('button',name='Expenses',exact=True).click()
 page.locator('[data-edit-record]').first.click()
 page.locator('#ex-amount').fill('4000.50')
 page.locator('#expense-form button[type="submit"]').click()
 page.get_by_role('button',name='Home',exact=True).click()
 page.locator('.hero-balance').get_by_text('৳45,999.5').wait_for()
 page.get_by_role('button',name='Reports',exact=True).click()
 page.get_by_text('Financial reports').wait_for()
 page.get_by_role('button',name='Settings',exact=True).click()
 page.locator('#tour-name').fill('SWE Tour 2026')
 page.get_by_role('button',name='Save details').click()
 page.get_by_text('SWE Tour 2026').first.wait_for()
 assert not errors,errors
 print('PASS: mobile interactive forms, create and edit, money calculations, reports tab, settings and visual render')
 print('Preview: /mnt/data/tour-money-preview.png')
 browser.close()
