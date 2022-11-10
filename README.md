# Github action to pass a flutter project only if test coverage is not less than 80%

## Example of usage

```yaml
name: Integration Test
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master

      - name: Setup Flutter
        uses: subosito/flutter-action@v1
        with:
          channel: "stable"

      - name: Cache Flutter dependencies
        uses: actions/cache@v1
        with:
          path: /opt/hostedtoolcache/flutter
          key: ${{ runner.OS }}-flutter-install-cache-${{ env.flutter_version }}

      - name: Install dependencies
        run: flutter pub get

      - name: Run tests
        run: flutter test --coverage

      ## This will break the workflow if test coverage < 80
      - name: HW1 test
        uses: EQSP-Task-Manager/hw1-draft@master
```
