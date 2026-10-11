# Retention edge cases

Policy cases to verify before enabling automated cleanup:

| Case | Expected behavior |
| --- | --- |
| Item age is one day below retention | Keep |
| Item age exactly equals retention | Treat as expired only if the policy defines the boundary as inclusive |
| Item age exceeds retention | Mark expired |
| Timestamp is missing or malformed | Do not silently delete; route to review |
| Clock is in the future | Flag for data-quality review |
| Preference or goal category is exempt | Preserve according to policy |
| Duplicate memories disagree | Reconcile before consolidating |

The existing retention decision helper is advisory and must not be treated as a deletion command.
