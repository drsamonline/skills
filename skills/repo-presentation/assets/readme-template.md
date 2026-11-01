# {{App name}}

<p>
  <a href="{{live url}}"><img alt="live: online" src="docs/assets/badge-live.svg"></a>
  <a href="{{repo}}/actions/workflows/test.yml"><img alt="tests: {{N}} passing" src="docs/assets/badge-tests.svg"></a>
  <a href="{{repo}}/actions/workflows/build-apps.yml"><img alt="build: green" src="docs/assets/badge-build.svg"></a>
  <a href="LICENSE"><img alt="licence: {{licence}}" src="docs/assets/badge-licence.svg"></a>
  <img alt="offline: no network" src="docs/assets/badge-offline.svg">
  <img alt="deps: {{n}} runtime" src="docs/assets/badge-deps.svg">
</p>

**{{One sentence: what it is, in the owner's own terms.}}**

**[Open the app →]({{live url}}/play/)** · [Landing page]({{live url}}/) · [The rule](#the-rule)

<!-- shot:start -->

![Screenshot](docs/shot.png)

<!-- shot:end -->

{{One short paragraph: offline? accounts? server? build step? dependencies?}}

## What it does

{{Two or three sentences, then the mechanic as a table or a short list.}}

| | |
|---|---|
| {{the numbers that matter}} | **{{n}}** |

## What it must not do, and does not

- {{the restraints, stated as rules rather than hopes}}

## Run it

```bash
node test-node.js
```

## Layout

```
docs/index.html         the landing page
docs/play/index.html    the app
docs/assets/            screenshots and generated badges
```

## Licence

{{licence}} — see `LICENSE`.
