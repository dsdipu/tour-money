# Tour Money Management — Beta v1.2

## Delivered

- Premium dark, responsive, four-tab financial app with quick expense entry.
- Single central fund, corrections, deposits, refunds, negative balance and audit history.
- Offline IndexedDB storage, 3 rolling automatic snapshots, separate pre-restore safety copy.
- Manual JSON backup export/import and read-only AirDrop-friendly viewer snapshot.
- Offline PDF (Latin text), Excel-compatible CSV and print-to-PDF report.
- iPhone Web Share integration when the browser supports sharing files.

## Changes from MVP 1.1

1. Make selection of expense category explicit to avoid accidentally classifying everything as Transport.
2. Native share sheet first for exports on capable devices; regular browser download fallback.
3. Strict calendar-date and backup schema validation.
4. Prevent reactivating a deleted initial fund while another initial fund is active.
5. Better wrapping for large Bangladeshi-currency amounts on small screens.
6. A dedicated first-use prompt for entering the total starting fund.

## Verification

- `node tests/smoke.cjs`: passed finance, precision, editing, backup, PDF and restore assertions.
- `python tests/ui_test.py`: passed simulated mobile UI interaction and screenshot rendering.
- `node --check app.js`: passed.
- Test environment blocks navigation via managed Chromium policy; genuine Service Worker, IndexedDB and iPhone features still need on-device verification.

## Known limitations

- No deployed HTTPS link is included. Host the project for free on GitHub Pages before installing on iPhone.
- No live local-network sync; President imports a read-only snapshot exported by VP (not secure access control).
- On-device automatic backups cannot recover data if device and browser storage are lost. Keep manual copies off-device.
- Built-in PDF maps non-Latin glyphs to `?`. Use `Print / Save PDF` for Bangla transaction names.
- Maximum iPhone compatibility rather than literally every iPhone/iOS version.
