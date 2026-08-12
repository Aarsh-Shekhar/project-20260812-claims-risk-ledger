# Operator Handoff

Domain: healthcare finance

This note records an implementation detail for Claims Risk Ledger. The current operating
threshold is `0.8` and review should happen within `48` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
