# TITMAS merge-blocking evidence-gate sandbox

Disposable public sandbox for one bounded TITMAS Agent Action Gate demonstration.

The ordinary test job can pass while the required `TITMAS Evidence Gate` blocks
merge when evidence was generated for an earlier commit. The demo uses the
repository variable `TITMAS_DEMO_EVIDENCE_SUBJECT_SHA` as a public, non-secret
subject selector so the same pull-request head can be rerun first with stale
commit-A evidence and then with corrected head-B evidence.

This repository is not a production deployment. A passing gate does not merge
the pull request and does not bypass any other GitHub rule.
