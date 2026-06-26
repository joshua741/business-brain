---
name: source-transcript-2026-06-24-morning-meeting-josh-mostafa
type: source
tags: [transcript, morning-meeting, mortgages, automation, disposition]
sources: [transcript-2026-06-24-morning-meeting-josh-mostafa.md]
updated: 2026-06-26
---

# Source: Morning Meeting Josh & Mostafa — 2026-06-24

**Summary**: Tighten-up day — Mercury/auto-pay confirmed across mortgages, GHL spam-call routing fixed, mortgage-sheet gaps (2nd position + servicing) identified, and 4302/4513 prepped for disposition.

**Sources**: transcript-2026-06-24-morning-meeting-josh-mostafa.md (manually relayed by Mostafa 2026-06-26)

**Last updated**: 2026-06-26

---

## Mortgages / banking
- All mortgages connected to **[[mercury]]** with **auto-pay** in place; DoorLoop accounts confirmed connected to [[sequence]].
- **[[4205-e-61st-st]]** mortgage was **overdue** (not yet pulled); **[[4302-e-61st-st]]** paid. Kenneth to have Shellpoint pull.
- Reserve→bank transfer dates set per property (Sequence rules), pending the AI-transfer migration.

## Mortgage sheet — second position + servicing (key gap)
- **[[4019-37th-st]]**: first position **$1,367.07** + second position **$176.67** = **total $1,543.74**. The sheet only tracked first position — flagged as a business-wide gap. Adding columns: **total payment (1st + 2nd + servicing)**, **second-position servicing yes/no**, **servicing amount**. The balance-alert threshold compares bank+reserve against this **total**.
- Second-position **servicing fees** vary by agreement and come out of WIH proceeds (shown on loan status, not charged on top).

## Disposition prep
- **[[4302-e-61st-st]]**: [[jalissa-ramos-mendoza|Jalissa]] lease pushed **inactive** in DoorLoop; Jalissa + Justin removed from GHL workflows. Website profile updated. **Rent-to-own terms: $1,450/mo, purchase $145,000, seller-finance down payment $35,922.50.** Application + listing link sent to prospect **[[glenda]]**.
- **Utilities** to be turned on for **[[4513-48th-st]]** and **[[4302-e-61st-st]]** (from the corresponding reserve accounts).

## Other
- **GHL spam/forwarding**: inbound calls were mis-forwarding to Josh's number; rerouted to **[[mkenzy]]** (hard-assigned). Fixed via the IVR/call-router.
- **[[3423-e-baylor-st]]**: refinanced — payment ~**$500 lower**; need new PITI + portal credentials from [[kenneth]].
- Reserve rules created for **[[2102-68th-st]]** and **[[4302-e-61st-st]]** on Sequence.
- **[[4626-s-lipscomb-st]]** irrevocable trust has **no EIN** (beneficiary [[webber-wealth-holdings]]) — confirmed.
- **[[3423-e-baylor-st]]** eviction (Veronica) scheduled the next morning (June 25).

## Related pages
- [[4019-37th-st]]
- [[4302-e-61st-st]]
- [[4205-e-61st-st]]
- [[4513-48th-st]]
- [[3423-e-baylor-st]]
- [[mercury]]
- [[mortgage-status-sheet]]
- [[glenda]]
- [[mkenzy]]
- [[mostafa]]
