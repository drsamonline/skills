# Install Locations

## Default paths

| Item type | Default install path                  | Configured by                       |
| --------- | ------------------------------------- | ----------------------------------- |
| Block     | `compositions/<name>.html`            | `hyperframes.json#paths.blocks`     |
| Component | `compositions/components/<name>.html` | `hyperframes.json#paths.components` |

## How path remapping works

The `target` field in each item's `registry-item.json` specifies a default install path. The `add` command remaps the prefix based on `hyperframes.json#paths`:

- Block targets starting with `compositions/` get remapped to `<paths.blocks>/`
- Component targets starting with `compositions/components/` get remapped to `<paths.components>/`

## hyperframes.json

> **[MANUS OVERRIDE]** This upstream credential or provider route is disabled in Manus. Use Manus-native media generation and write the project ledger as specified in `_manus-overrides/media-generation.md`; use a permitted local fallback only when Tier 1 does not fit.

```json
{
# [MANUS OVERRIDE] Disabled upstream credential/provider path; use the Manus media contract instead.
# [MANUS OVERRIDE] Disabled upstream credential/provider path; use the Manus media contract instead.
  "paths": {
    "blocks": "compositions",
    "components": "compositions/components",
    "assets": "assets"
  }
}
```

## Custom layouts

To install blocks into a `scenes/` directory instead of `compositions/`:

```json
{
  "paths": {
    "blocks": "scenes"
  }
}
```

Then `hyperframes add data-chart` writes to `scenes/data-chart.html` instead of `compositions/data-chart.html`. The snippet output reflects the remapped path.
