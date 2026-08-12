# Connector capability reference — Zapier, Notion, Linear MCPs (verified July 2026)

What each Super Magic MCP connector can actually do, verified against official docs and
live servers. This is the raw material for connector-dependent skills.

## Zapier MCP

9,000+ apps / 30,000+ actions. Two modes: dynamic discovery (agent searches the catalog and
enables actions mid-conversation) or curated servers (admin pins exact tools, can lock field
values — e.g. pin "Send Channel Message" to one channel). Each successful call = 2 Zapier
tasks. App credentials live in Zapier's managed layer; SOC 2; all calls logged.

### Microsoft ecosystem (verified action inventories)

| App | Highlights | Gaps |
|---|---|---|
| **Outlook** (51 actions) | Send/Reply/Forward/Draft email, folders, flags, categories, distribution lists; Create/Update/Delete Event, Add Attendees; contacts CRUD; Find Emails/Events/Contacts, Get Attachment | — |
| **Teams** (28) | Send Channel/Chat/Bot message, message cards, **Send Approval Request and Wait**, create channels/chats, set status; Find member/channel triggers | No meeting scheduling (use Outlook Create Event) |
| **SharePoint** (34) | Upload/Replace/Move files, folders, list items CRUD, pages, **sharing links/invitations, remove permissions**; Find file/list/site | — |
| **OneDrive** | File CRUD, sharing links, **KQL search**, permissions | — |
| **Excel** | Add/Update/Clear rows, tables, worksheets; Find Row, Get Range | — |
| **Entra ID** | **Create/Update/Disable/Delete User, group membership** | No user *search*; writes only + New User trigger |
| **To Do** | Create/Complete Task, lists, Find Task | — |
| **Bookings** | ❌ NO Zapier integration exists | Use Calendly or Outlook Calendar |
| **Planner** | ❌ NO Zapier integration exists | Use To Do / Linear / Jira |

### Other verified high-value apps

- **Slack**: full message/channel/canvas suite + **Request Approval**, reminders, statuses
- **Calendly** (best Bookings substitute): **Create One-Off Meeting Link**, Book Meeting for Invitee, cancel, no-show, routing forms, meeting recap + transcript search
- **QuickBooks**: invoices (create/send/void), estimates, payments, **Create Time Activity**, customers/vendors, expenses, attach files; rich Find actions
- **Xero**: invoices/quotes/bills/payments/credit notes/POs, repeating invoices, attachments
- **Stripe**: customers, invoices, **payment links**, checkout, subscriptions; find charges/balance
- **HubSpot** (45): tickets, contacts, companies, deals, associations, lists/workflows
- **Salesforce**: records CRUD, **SOQL/SOSL queries**, Run Report, Launch Flow, Send Email
- **Twilio**: Send SMS / WhatsApp / outbound voice call with spoken message
- **DocuSign**: signature requests, envelopes from template, bulk send, void, download docs
- **Jira**: create/update issues, comments, attachments, work logs, sprints, **JQL search**
- **ServiceNow**: table-level record CRUD + find (covers incident/request/change)
- **PagerDuty**: trigger/acknowledge/resolve events, **Find User on Call**
- **Dropbox**: file ops + **File Request** (collect logs from users), expiring password-protected links
- **Zoom**: create meeting, registrants, **Get Meeting Summary**, find recordings
- **Gmail / Google Calendar / Drive / Sheets / Forms**: full suites; Calendar has **Find Busy Periods**
- **Typeform**: create/duplicate forms, lookup responses (CSAT loop)
- **SmileBack**: ❌ legacy Zapier app removed; use native PSA integration
- **Opsgenie**: Create Alert only (thin)
- Plus observed in production already: **Firecrawl** (scrape/crawl/extract/search/agent)

## Notion MCP (hosted, mcp.notion.com)

20 tools, verified: notion-search (semantic, incl. connected Slack/GDrive/Jira with Notion AI),
notion-fetch, notion-create-pages, notion-update-page, notion-move-pages, notion-duplicate-page,
notion-create-database, notion-update-data-source, notion-create-view (table/board/calendar/
timeline/gallery/**form**/chart/dashboard), notion-update-view, notion-query-data-sources (SQL,
Business+), notion-query-database-view, notion-query-meeting-notes, notion-create-comment,
notion-get-comments, notion-get-teams, notion-get-users, notion-create/download-attachment,
notion-get-async-task.

Limits: ~180 req/min/user; search 30/min; SQL + meeting-notes tools need Business+ w/ Notion AI.
OAuth scoped to the authorizing user's access.

## Linear MCP (hosted, mcp.linear.app)

23 verified tools: list/get/create/update_issue, list_my_issues, list/create_comment,
list_issue_statuses, get_issue_status, list/create_issue_label, list/get/create/update_project,
list_project_labels, list_cycles, list/get_team, list/get_user, list/get_document,
search_documentation. Feb 2026 additions (capabilities, names unverified): initiatives,
initiative updates, project milestones, project updates, image/resource loading.

Auth: OAuth 2.1 or API-key bearer; scoped to user permissions; priority enum 0–4;
~1,500 req/hr/user.

## Design implications for skills

1. Zapier's approval actions (Teams "Send Approval Request and Wait", Slack "Request Approval")
   give write-heavy skills a native human-in-the-loop gate outside Thread.
2. Entra ID writes without search → onboarding/offboarding skills must resolve identity from
   the PSA/ticket side first, then write to Entra.
3. Calendly one-off links replace the missing Bookings integration for "book a tech" flows.
4. QuickBooks Create Time Activity + Thread log_time_entry = ticket→invoice reconciliation.
5. Notion form views + data-source queries = structured intake without another form vendor.
6. Linear closes the loop MSPs currently lack: recurring ticket pattern → engineering issue →
   fix shipped → notify every affected ticket.
