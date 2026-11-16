# Tour Money — Confirmed Requirements (from 36 decisions)

## Scope
- Single department tour; fewer than 50 participants.
- Total initial fund entered once, because everybody has paid already; no participant-ledger requirement.
- One main editor (VP), president sees a separate read-only **snapshot**; local live sync optional and not in MVP.
- Android + iPhone, mainly iPhone. Free first install may require Internet; financial operations work offline thereafter.
- Maximum practical support for iPhone models, subject to iOS browser features.
- No password, PIN or login. English app UI; user-entered expense details may be Bangla.

## Financial ledger
- BDT, Bangladeshi lakh grouping, decimals only when needed; calculations use integer paisa.
- Initial fund, additional deposit, signed corrections, refund payouts, and real expenses.
- Single combined balance; no separate wallets or payment-method tracking.
- Negative balance allowed without alert.
- No planned budgets, participant dues or pending-payment commitments.
- Remaining balance shown at the end of the tour; no special settlement system.

## Transactions
- Quick expense-entry bottom sheet, with mandatory title, category, and amount; optional note.
- Date/time defaults to device time and can be manually edited.
- Default categories plus rename/archive/add custom categories.
- Basic title search, newest/oldest sort; expense edits, soft-delete and restore with complete audit trail.
- Confirmation before deletions.

## Dashboard and reports
- Premium dark design, tabs: Home, Expenses, Reports, Settings.
- Advanced statistics: fund, expenses, remaining, utilization, categories, daily trend and largest expense.
- Reports date-range filters independent of basic transaction search.
- Offline PDF and Excel-compatible CSV report export, print-friendly report alternative.
- No financial warnings or push notifications.
- Editable tour name and department name only.

## Data and sharing
- Local IndexedDB. Instant save after a transaction.
- Transaction-triggered automatic snapshots, latest 3 only.
- JSON manual export/import. Restore makes a separate safety copy first.
- Read-only JSON snapshot transfer to another phone through AirDrop/Files.
- Real-time local Wi-Fi/Hotspot sharing is optional; not built in Beta 1.2.

## MVP implementation details / constraints
- Static PWA, no server-side ledger and no paid hosting required.
- HTTPS site needed for initial installation and service-worker caching.
- Device loss, app removal or iOS storage eviction can erase on-device data: manual off-device backup required.
- Real iPhone tests are outstanding; compatibility with literally all models cannot be guaranteed.
- Built-in PDF uses basic Latin fonts; system Print / Save PDF better supports Unicode titles.

## Implementation progress

- Beta v1.2 includes the single-device financial application, offline PWA shell, category & transaction editing, reports and read-only snapshot file transfer.
- Not in beta: live phone-to-phone local Wi-Fi sync, iPhone hardware validation, App Store packaging.
- Initial install must be hosted on HTTPS to support PWA offline caching; the project provides deployable static files, not a hosted public URL.
