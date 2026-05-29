# Paste — May 16, 2026 8:48 AM — Content AI Script

**Description:** Pasted text file from May 2026 — Content AI Google Apps Script for Rent2OwnCribs automation.
**Date:** May 16, 2026

## Content

This file contains the Google Apps Script code for the Rent2OwnCribs Content System automation. Key functions:

### Core Functions

**onEdit(e)** — Auto-logs every change to a Google Sheet tab:
- Tracks Status changes in Daily Queue (Approved/Denied/Posted/Revision Requested)
- Logs Knowledge Base entries, Audience Questions, Brand Intelligence updates
- All edits automatically logged to Audit Log tab

**onOpen()** — Creates custom menu "Content Studio" with submenus:
- Daily Queue: Approve, Deny, Mark as Posted, Request Revision, Queue Summary
- Knowledge Base: Add Entry, Mark as Verified
- Audience Questions: Mark Answered, Create Post from Question
- Schedule: Fill Next Slot, Show Schedule Summary
- Execute & Run: Run Now, Test Run, Schedule Post, Execute Row, Run Full Automation
- Audit Log: Summary, Clear Old Entries (30+ days)
- Dashboard Refresh
- Weekly Summary Email

### Key Actions

**approveSelectedPost()** — Marks selected Daily Queue row as Approved, colors green, logs audit

**denySelectedPost()** — Prompts for denial reason, marks as Denied, colors red

**markSelectedPosted()** — Marks as Posted, records date, copies to Approved Library

**requestRevisionSelected()** — Prompts for revision notes, marks Revision Requested, colors yellow

**addKnowledgeEntry()** — Prompts for topic/content/category, adds to Knowledge Base with auto-ID

**markQuestionAnswered()** — Records answer for audience question, marks Answered

**createPostFromQuestion()** — Creates a Daily Queue post from an audience question

**sendWeeklySummaryEmail()** — Sends weekly content system summary email with queue stats

**logAudit(action, tab, details, oldValue, newValue, user)** — Core audit logging function

### Sheet Structure Expected
- Daily Queue
- Knowledge Base
- Audience Questions
- Brand Intelligence
- Pre-Schedule Builder
- References & Inspiration
- Source URLs
- Daily Content Identity
- Monthly Content Identity
- Dashboard
- Approved Library
- Audit Log

## Context
This is the Google Apps Script powering the Content AI automation for Rent2OwnCribs social media. Approval/denial workflow runs through this script in the Google Sheet before content is posted to social media platforms.
