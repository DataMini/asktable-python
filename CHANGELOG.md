# Changelog

## 5.5.0 (2025-07-19)

Full Changelog: [v5.4.0...v5.5.0](https://github.com/DataMini/asktable-python/compare/v5.4.0...v5.5.0)

### Features

* **api:** add test set api ([cf653ef](https://github.com/DataMini/asktable-python/commit/cf653ef0d527894151c209f7eb79b120e8d7109c))
* **api:** api update ([d7a73bc](https://github.com/DataMini/asktable-python/commit/d7a73bceb38896da2565dd7e1ae8a3e39529a685))
* clean up environment call outs ([6002d27](https://github.com/DataMini/asktable-python/commit/6002d277b7004e7fdd69f8b23572cf84a6cf10da))
* **client:** add follow_redirects request option ([b22320b](https://github.com/DataMini/asktable-python/commit/b22320bad43f0de89af6d252c36902b2cd08ec97))
* **client:** add support for aiohttp ([292b89e](https://github.com/DataMini/asktable-python/commit/292b89e54d3215237251f84ebbae97d4cbf65310))


### Bug Fixes

* **ci:** correct conditional ([b23a053](https://github.com/DataMini/asktable-python/commit/b23a0530daffe5b27939e7ab9516790f6fb36a7b))
* **ci:** release-doctor — report correct token name ([71f15b7](https://github.com/DataMini/asktable-python/commit/71f15b7d055dafd7aabb993d5ca0f6ca33707620))
* **client:** correctly parse binary response | stream ([5568773](https://github.com/DataMini/asktable-python/commit/5568773fc1b6ee7a5183cd5e6789ce6eafe119e8))
* **client:** don't send Content-Type header on GET requests ([41feabc](https://github.com/DataMini/asktable-python/commit/41feabcb23fb5c257d18ba7f96f0ddb9304d53d5))
* **docs/api:** remove references to nonexistent types ([7d673d4](https://github.com/DataMini/asktable-python/commit/7d673d44b295a507ca08ff0982cc5e033893e3d3))
* **pagination:** correct next page check ([03552e7](https://github.com/DataMini/asktable-python/commit/03552e74ca1fa48289b48381777b1243398777bc))
* **parsing:** correctly handle nested discriminated unions ([5fcaeb7](https://github.com/DataMini/asktable-python/commit/5fcaeb76ff37258c12becb7e459a3cfa56988fc0))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([3036c4b](https://github.com/DataMini/asktable-python/commit/3036c4bdbe59cd13bdfacdd113478e3e6ddd8ca0))


### Chores

* **ci:** change upload type ([267f707](https://github.com/DataMini/asktable-python/commit/267f707806319c9b4499046f286f891a985d22de))
* **ci:** enable for pull requests ([a6636e7](https://github.com/DataMini/asktable-python/commit/a6636e7b8409f7750b52c4850f05be437e4ed31d))
* **ci:** only run for pushes and fork pull requests ([f5756ca](https://github.com/DataMini/asktable-python/commit/f5756ca55464cba7219498f0fcf0786d299fdc7d))
* **docs:** remove reference to rye shell ([9fc4749](https://github.com/DataMini/asktable-python/commit/9fc4749e8965d398f281078e14f0249d12571ace))
* **docs:** remove unnecessary param examples ([d2875f3](https://github.com/DataMini/asktable-python/commit/d2875f3438404557c839e0d158a2e573c3607f1f))
* **internal:** bump pinned h11 dep ([cb54577](https://github.com/DataMini/asktable-python/commit/cb545771166f525600c876d70e6ca9af74aada7f))
* **internal:** codegen related update ([c281941](https://github.com/DataMini/asktable-python/commit/c28194157b0e93b082fc5c441528a4bdc0640c00))
* **internal:** codegen related update ([65ea7c5](https://github.com/DataMini/asktable-python/commit/65ea7c536f5fe17dfb13666bf7e37f25bf470bd9))
* **internal:** update conftest.py ([f06435d](https://github.com/DataMini/asktable-python/commit/f06435ded63522ac7f30d47b560183b86e95ef27))
* **package:** mark python 3.13 as supported ([e1a20f7](https://github.com/DataMini/asktable-python/commit/e1a20f7a5f7ce9dee0d182c2addc5fcf8b4342ae))
* **readme:** fix version rendering on pypi ([e05e6e5](https://github.com/DataMini/asktable-python/commit/e05e6e562cfddd5ef7b3ee27a2a155e0e8305e6c))
* **readme:** update badges ([bc28102](https://github.com/DataMini/asktable-python/commit/bc281028397ea60d93f86ea563e3e9cba303b0c6))
* **tests:** add tests for httpx client instantiation & proxies ([c620e09](https://github.com/DataMini/asktable-python/commit/c620e09f4be03fabc31167839018e69b8d7f5d7b))
* **tests:** run tests in parallel ([9d9d65e](https://github.com/DataMini/asktable-python/commit/9d9d65e5be80faba732cd2d29854186ff565b4c7))
* **tests:** skip some failing tests on the latest python versions ([188abef](https://github.com/DataMini/asktable-python/commit/188abef74adcaf1c5b8b4ee8b39315aba98c7f95))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([482e328](https://github.com/DataMini/asktable-python/commit/482e328e4938b04c3eca656984857d2ffc302fa3))

## 5.4.0 (2025-05-27)

Full Changelog: [v5.3.1...v5.4.0](https://github.com/DataMini/asktable-python/compare/v5.3.1...v5.4.0)

### Features

* **api:** api update ([84767d7](https://github.com/DataMini/asktable-python/commit/84767d7648a7df94f1caf85628576ea948d94475))
* **api:** api update ([558ab83](https://github.com/DataMini/asktable-python/commit/558ab837046be3f9e902a2e073096217bda1438e))
* **api:** api update ([07d802a](https://github.com/DataMini/asktable-python/commit/07d802a94360a7e66e0594b5ba39b9fc4916a56d))
* **api:** api update ([18a5eaf](https://github.com/DataMini/asktable-python/commit/18a5eafaf07afc7c59141e957104728fe2d413b5))
* **api:** api update ([dc90fe3](https://github.com/DataMini/asktable-python/commit/dc90fe3f3b0829913fde1a288eb8f3ff6fbf7e6d))
* **api:** api update ([8fda6da](https://github.com/DataMini/asktable-python/commit/8fda6da68f5c439b69572ad06df119915475acd4))
* **api:** api update ([8cfc989](https://github.com/DataMini/asktable-python/commit/8cfc98987196f71dc9b1ac788a66e7fb7a6b62c9))
* **api:** api update ([317b682](https://github.com/DataMini/asktable-python/commit/317b682b9de2a8803f8d2be7be7a9ed8ad1e961c))


### Bug Fixes

* **package:** support direct resource imports ([e082d60](https://github.com/DataMini/asktable-python/commit/e082d60e17dacc06f1a3091454db8d522bf8e7a2))
* **perf:** optimize some hot paths ([4ce95f7](https://github.com/DataMini/asktable-python/commit/4ce95f7c3a5f0b7568ad63d0bb6fe8dade3d20ff))
* **perf:** skip traversing types for NotGiven values ([00250bb](https://github.com/DataMini/asktable-python/commit/00250bbfc900cb7003e3e77239ced58934b6d826))
* **pydantic v1:** more robust ModelField.annotation check ([c16373d](https://github.com/DataMini/asktable-python/commit/c16373dba54d24f705650aa38d3b4c1a772f23ff))


### Chores

* broadly detect json family of content-type headers ([3bff15d](https://github.com/DataMini/asktable-python/commit/3bff15dcccae660478bd3e6a30aa609e4bcc186f))
* **ci:** add timeout thresholds for CI jobs ([f51cedc](https://github.com/DataMini/asktable-python/commit/f51cedc6e85b7300ae989972c02c2f4303c7838a))
* **ci:** fix installation instructions ([02f7bb0](https://github.com/DataMini/asktable-python/commit/02f7bb02172f9ac58153e92c2acc063c876fd63b))
* **ci:** only use depot for staging repos ([6c155eb](https://github.com/DataMini/asktable-python/commit/6c155eb595e7227c769e953a5040b577f85f494c))
* **ci:** upload sdks to package manager ([ed6c603](https://github.com/DataMini/asktable-python/commit/ed6c603a22bc79cf74791566cef81b536dc0d0b3))
* **client:** minor internal fixes ([b4af709](https://github.com/DataMini/asktable-python/commit/b4af709160aa14f36bef3a624c069b21290ded66))
* **docs:** grammar improvements ([8f09ac8](https://github.com/DataMini/asktable-python/commit/8f09ac84dd9df377925ec5ed214037c1c5b23d48))
* **internal:** avoid errors for isinstance checks on proxies ([79c1774](https://github.com/DataMini/asktable-python/commit/79c1774d4d811f45d947711c509911d5b0880e72))
* **internal:** base client updates ([7e7f8c5](https://github.com/DataMini/asktable-python/commit/7e7f8c56783a125505f587d6f206da00da98f438))
* **internal:** bump pyright version ([b56ec6c](https://github.com/DataMini/asktable-python/commit/b56ec6cc156694361cbd43a2d8590813f30a47c0))
* **internal:** codegen related update ([3719d1b](https://github.com/DataMini/asktable-python/commit/3719d1bf1db482d5f08368b6162d67c878e48369))
* **internal:** fix list file params ([12bba1b](https://github.com/DataMini/asktable-python/commit/12bba1b329d0149f1b8065c983efbddda6a1a1d1))
* **internal:** import reformatting ([bb1b5a8](https://github.com/DataMini/asktable-python/commit/bb1b5a84fbea13e655f968639f3e5edf584914ad))
* **internal:** minor formatting changes ([1f83169](https://github.com/DataMini/asktable-python/commit/1f83169570f13ba1ede9c92a23e610018d39f8e0))
* **internal:** refactor retries to not use recursion ([af64ff0](https://github.com/DataMini/asktable-python/commit/af64ff050f75fae9c6368c6c0d105197f227397c))
* **internal:** update models test ([4e84f01](https://github.com/DataMini/asktable-python/commit/4e84f01f5b52e119f73cab72e4ea3ceaa1889e42))
* **internal:** update pyright settings ([c1a4b25](https://github.com/DataMini/asktable-python/commit/c1a4b25eda6192bfb974f1aa6b21ae35f4ea762e))

## 5.3.1 (2025-04-10)

Full Changelog: [v5.3.0...v5.3.1](https://github.com/DataMini/asktable-python/compare/v5.3.0...v5.3.1)

### Bug Fixes

* **api:** update default base_url ([85ff425](https://github.com/DataMini/asktable-python/commit/85ff4250da2b704eaae667d2020e0b842214861d))


### Chores

* **internal:** expand CI branch coverage ([7117507](https://github.com/DataMini/asktable-python/commit/7117507899b9a4e10417d3e8588827ca48706b07))
* **internal:** reduce CI branch coverage ([842b93d](https://github.com/DataMini/asktable-python/commit/842b93d52f827e7b1f6ee3f080b3de3f9965fbdf))

## 5.3.0 (2025-04-09)

Full Changelog: [v5.2.0...v5.3.0](https://github.com/DataMini/asktable-python/compare/v5.2.0...v5.3.0)

### Features

* **api:** api update ([#187](https://github.com/DataMini/asktable-python/issues/187)) ([645b80a](https://github.com/DataMini/asktable-python/commit/645b80a780d0409c0368ab2ec7d4c811b4bb74ac))
* **api:** api update ([#188](https://github.com/DataMini/asktable-python/issues/188)) ([ebd0446](https://github.com/DataMini/asktable-python/commit/ebd044644cd2bd152456b124e4b356cd08bfdc76))
* **api:** api update ([#190](https://github.com/DataMini/asktable-python/issues/190)) ([fabff6d](https://github.com/DataMini/asktable-python/commit/fabff6d4a56673e1c6b60744e88607fc773abc55))
* **api:** api update ([#191](https://github.com/DataMini/asktable-python/issues/191)) ([0270755](https://github.com/DataMini/asktable-python/commit/0270755b827e9ea9227ce977e026fefaf1189da0))
* **api:** api update ([#192](https://github.com/DataMini/asktable-python/issues/192)) ([d6d57bc](https://github.com/DataMini/asktable-python/commit/d6d57bcf4eb98b8adb76508963ecc6a7ac2aaa01))
* **api:** api update ([#196](https://github.com/DataMini/asktable-python/issues/196)) ([addbcf9](https://github.com/DataMini/asktable-python/commit/addbcf9cdb9d3f6c710ac53f94b529c236eaa5c0))


### Bug Fixes

* **ci:** ensure pip is always available ([#185](https://github.com/DataMini/asktable-python/issues/185)) ([1bf7016](https://github.com/DataMini/asktable-python/commit/1bf701617a81109d6071e06f09910349544cbf6f))
* **ci:** remove publishing patch ([#186](https://github.com/DataMini/asktable-python/issues/186)) ([077f917](https://github.com/DataMini/asktable-python/commit/077f9172189fb51d058fdaf48671d1c74d1c73cf))


### Chores

* fix typos ([#189](https://github.com/DataMini/asktable-python/issues/189)) ([f294618](https://github.com/DataMini/asktable-python/commit/f294618bf32edd5a19f1a357f13e78e4c0fec096))
* **internal:** codegen related update ([#195](https://github.com/DataMini/asktable-python/issues/195)) ([fb83cf4](https://github.com/DataMini/asktable-python/commit/fb83cf4102ccb7da31a7f66419aa937db9338982))
* **internal:** minor test fixes ([#193](https://github.com/DataMini/asktable-python/issues/193)) ([4483c2f](https://github.com/DataMini/asktable-python/commit/4483c2fefd7f57ed9dfaebc62f4b3d5677d282ee))
* **internal:** remove trailing character ([#194](https://github.com/DataMini/asktable-python/issues/194)) ([27b9d4f](https://github.com/DataMini/asktable-python/commit/27b9d4fbd4a9579c98faa74a75fe87a77489e1b2))
* **internal:** slight transform perf improvement ([#197](https://github.com/DataMini/asktable-python/issues/197)) ([1f09d5b](https://github.com/DataMini/asktable-python/commit/1f09d5b9d3e0119efdbed970898899428406fb29))
* remove custom code ([746f693](https://github.com/DataMini/asktable-python/commit/746f6936a501d656086f6342abed4a54ab07be96))
* slight wording improvement in README ([#199](https://github.com/DataMini/asktable-python/issues/199)) ([9424bae](https://github.com/DataMini/asktable-python/commit/9424bae54d01f1f69cf148f7e941e2149b90b905))
* **tests:** improve enum examples ([#198](https://github.com/DataMini/asktable-python/issues/198)) ([133aa56](https://github.com/DataMini/asktable-python/commit/133aa566654b70214d489a66ab929a17edf93918))

## 5.2.0 (2025-03-17)

Full Changelog: [v5.1.0...v5.2.0](https://github.com/DataMini/asktable-python/compare/v5.1.0...v5.2.0)

### Features

* **api:** api update ([#180](https://github.com/DataMini/asktable-python/issues/180)) ([e14c5cd](https://github.com/DataMini/asktable-python/commit/e14c5cd1fbea464aee0e71697c0fd966da6b1a9b))
* **api:** api update ([#182](https://github.com/DataMini/asktable-python/issues/182)) ([dde8d1f](https://github.com/DataMini/asktable-python/commit/dde8d1f767e61d2a2ca6b57c8a1133285b62fe24))

## 5.1.0 (2025-03-15)

Full Changelog: [v5.0.0...v5.1.0](https://github.com/DataMini/asktable-python/compare/v5.0.0...v5.1.0)

### Features

* Update publish-pypi.yml ([dd3bc4d](https://github.com/DataMini/asktable-python/commit/dd3bc4d77fdb5f8d2ff6fcedf80d6070c775c800))

## 5.0.0 (2025-03-15)

Full Changelog: [v4.7.0...v5.0.0](https://github.com/DataMini/asktable-python/compare/v4.7.0...v5.0.0)

### Features

* **api:** manual updates ([#173](https://github.com/DataMini/asktable-python/issues/173)) ([dba48e1](https://github.com/DataMini/asktable-python/commit/dba48e1aebe2abab983f6fe802d8605abdab82ac))
* **api:** manual updates ([#175](https://github.com/DataMini/asktable-python/issues/175)) ([64bd21f](https://github.com/DataMini/asktable-python/commit/64bd21ff24dbc8a8495a48c73207fbeab1ac5082))


### Chores

* remove custom code ([c1a8142](https://github.com/DataMini/asktable-python/commit/c1a81420aeb2a7eb8c6f0b32c8f84134a50e0a37))

## 4.7.0 (2025-03-15)

Full Changelog: [v4.6.0...v4.7.0](https://github.com/DataMini/asktable-python/compare/v4.6.0...v4.7.0)

### Features

* **api:** manual updates ([#170](https://github.com/DataMini/asktable-python/issues/170)) ([8a4111d](https://github.com/DataMini/asktable-python/commit/8a4111db0c9fd229e30032ccfbdedd6556d49710))

## 4.6.0 (2025-03-15)

Full Changelog: [v4.5.0...v4.6.0](https://github.com/DataMini/asktable-python/compare/v4.5.0...v4.6.0)

### Features

* **api:** api update ([#144](https://github.com/DataMini/asktable-python/issues/144)) ([668a25d](https://github.com/DataMini/asktable-python/commit/668a25dd349090c2f095d068a0ada72587aac38f))
* **api:** manual updates ([#167](https://github.com/DataMini/asktable-python/issues/167)) ([06c63d2](https://github.com/DataMini/asktable-python/commit/06c63d292a5278295e93c4d7a65cf25b02234e2b))
* **api:** manual updates ([#168](https://github.com/DataMini/asktable-python/issues/168)) ([8990ba9](https://github.com/DataMini/asktable-python/commit/8990ba9c162f2224e23e8db58646f2c485f77e1c))
* **client:** allow passing `NotGiven` for body ([#155](https://github.com/DataMini/asktable-python/issues/155)) ([153f86b](https://github.com/DataMini/asktable-python/commit/153f86b5c5c0099edc9b0622ebe36553b653e8ca))
* **client:** send `X-Stainless-Read-Timeout` header ([#149](https://github.com/DataMini/asktable-python/issues/149)) ([2bbef8d](https://github.com/DataMini/asktable-python/commit/2bbef8d335a87602e14fbea387f3b7fe136424f0))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#153](https://github.com/DataMini/asktable-python/issues/153)) ([92577a2](https://github.com/DataMini/asktable-python/commit/92577a2765975e59273e218ba20c93cbed7a05c1))
* **client:** mark some request bodies as optional ([153f86b](https://github.com/DataMini/asktable-python/commit/153f86b5c5c0099edc9b0622ebe36553b653e8ca))
* improve names for conflicting params ([#148](https://github.com/DataMini/asktable-python/issues/148)) ([3f9650f](https://github.com/DataMini/asktable-python/commit/3f9650f5519444a1517dcf85bf313780e5dd6cce))
* **types:** handle more discriminated union shapes ([#166](https://github.com/DataMini/asktable-python/issues/166)) ([850d425](https://github.com/DataMini/asktable-python/commit/850d425cf365d48cc9f7a41d09d295e8547befdf))


### Chores

* **docs:** update client docstring ([#159](https://github.com/DataMini/asktable-python/issues/159)) ([5a0da4d](https://github.com/DataMini/asktable-python/commit/5a0da4dd6288d7d55b7b2d4585b12e876d384423))
* **internal:** bummp ruff dependency ([#147](https://github.com/DataMini/asktable-python/issues/147)) ([9638e50](https://github.com/DataMini/asktable-python/commit/9638e50e2a5325ba4cb66e8cd987d96da80f37d5))
* **internal:** bump rye to 0.44.0 ([#165](https://github.com/DataMini/asktable-python/issues/165)) ([5ead610](https://github.com/DataMini/asktable-python/commit/5ead610c43bcde3e61ec6e2e6e4fd892be1f4e59))
* **internal:** change default timeout to an int ([#146](https://github.com/DataMini/asktable-python/issues/146)) ([f418605](https://github.com/DataMini/asktable-python/commit/f41860576a0d6e8ce78352de1e997c3e8149a52f))
* **internal:** codegen related update ([#138](https://github.com/DataMini/asktable-python/issues/138)) ([e70fbf4](https://github.com/DataMini/asktable-python/commit/e70fbf41048ca082ffd9f4888ccfa7bd9f97c57f))
* **internal:** codegen related update ([#141](https://github.com/DataMini/asktable-python/issues/141)) ([56d0462](https://github.com/DataMini/asktable-python/commit/56d0462efef6c92a6727fd91c638a19750195d4e))
* **internal:** codegen related update ([#154](https://github.com/DataMini/asktable-python/issues/154)) ([2242fad](https://github.com/DataMini/asktable-python/commit/2242fad33cc31d4bf434bc6161ca444c7cf3bf36))
* **internal:** codegen related update ([#164](https://github.com/DataMini/asktable-python/issues/164)) ([1cb3903](https://github.com/DataMini/asktable-python/commit/1cb390324e6894374519e8062b446873d138cde0))
* **internal:** fix devcontainers setup ([#156](https://github.com/DataMini/asktable-python/issues/156)) ([944423e](https://github.com/DataMini/asktable-python/commit/944423e7d0c69dcf0a54141ce69127db2369b247))
* **internal:** fix type traversing dictionary params ([#150](https://github.com/DataMini/asktable-python/issues/150)) ([0caeb28](https://github.com/DataMini/asktable-python/commit/0caeb28b8647a9753b16bbc8a2963f900e4dd9d2))
* **internal:** minor formatting changes ([#143](https://github.com/DataMini/asktable-python/issues/143)) ([a4ac34f](https://github.com/DataMini/asktable-python/commit/a4ac34fcf7a8350bdd03b5c51917ca5896183c63))
* **internal:** minor style changes ([#142](https://github.com/DataMini/asktable-python/issues/142)) ([cb5834c](https://github.com/DataMini/asktable-python/commit/cb5834c4e4819f6c9a99dcd9a9d8296b413d0317))
* **internal:** minor type handling changes ([#151](https://github.com/DataMini/asktable-python/issues/151)) ([67e6469](https://github.com/DataMini/asktable-python/commit/67e6469d84d6fc761ae2e7fc55d47ffb07c49309))
* **internal:** properly set __pydantic_private__ ([#157](https://github.com/DataMini/asktable-python/issues/157)) ([30a260f](https://github.com/DataMini/asktable-python/commit/30a260f78f2b32e82467afe05703e2f8aa88fc68))
* **internal:** remove extra empty newlines ([#163](https://github.com/DataMini/asktable-python/issues/163)) ([d8b30ce](https://github.com/DataMini/asktable-python/commit/d8b30cec54b715e20a90de84a4a3393a0b556c33))
* **internal:** remove unused http client options forwarding ([#160](https://github.com/DataMini/asktable-python/issues/160)) ([298eb9c](https://github.com/DataMini/asktable-python/commit/298eb9ca830efd80ca27e868a0081ff4822dc2db))
* **internal:** update client tests ([#152](https://github.com/DataMini/asktable-python/issues/152)) ([02af016](https://github.com/DataMini/asktable-python/commit/02af016ec2d3f945765bbc76a24a0a102757b966))


### Documentation

* **raw responses:** fix duplicate `the` ([#140](https://github.com/DataMini/asktable-python/issues/140)) ([5580989](https://github.com/DataMini/asktable-python/commit/55809895dc745aa046c93493ad7f658ed652c869))
* revise readme docs about nested params ([#161](https://github.com/DataMini/asktable-python/issues/161)) ([c4a4e34](https://github.com/DataMini/asktable-python/commit/c4a4e34b3ddc3a19aac34cd4f167af53e2665933))
* update URLs from stainlessapi.com to stainless.com ([#158](https://github.com/DataMini/asktable-python/issues/158)) ([a8ee0e2](https://github.com/DataMini/asktable-python/commit/a8ee0e203076b01180be2c164174a469c2f444ef))

## 4.5.0 (2025-01-19)

Full Changelog: [v4.4.0...v4.5.0](https://github.com/DataMini/asktable-python/compare/v4.4.0...v4.5.0)

### Features

* **api:** api update ([#134](https://github.com/DataMini/asktable-python/issues/134)) ([6d30087](https://github.com/DataMini/asktable-python/commit/6d30087ca2351d75443935907e7749fdfc96d1cf))
* **api:** update organization info ([#135](https://github.com/DataMini/asktable-python/issues/135)) ([bad8bba](https://github.com/DataMini/asktable-python/commit/bad8bba976aa94114c4b6a801b31189913aa7699))


### Bug Fixes

* type hint in custom code ([643d5c2](https://github.com/DataMini/asktable-python/commit/643d5c274950f7a6af11e5c1a8127ce70db82ada))


### Chores

* **internal:** codegen related update ([#132](https://github.com/DataMini/asktable-python/issues/132)) ([f167bd7](https://github.com/DataMini/asktable-python/commit/f167bd73704e7e7c372ecc3aa73a64efbaa0d13b))

## 4.4.0 (2025-01-15)

Full Changelog: [v4.3.0...v4.4.0](https://github.com/DataMini/asktable-python/compare/v4.3.0...v4.4.0)

### Features

* **api:** api update ([#129](https://github.com/DataMini/asktable-python/issues/129)) ([005b72f](https://github.com/DataMini/asktable-python/commit/005b72fb886bbabb2c5e09a04a029bc127587414))

## 4.3.0 (2025-01-11)

Full Changelog: [v4.2.0...v4.3.0](https://github.com/DataMini/asktable-python/compare/v4.2.0...v4.3.0)

### Features

* Update datasources.py ([d4618e4](https://github.com/DataMini/asktable-python/commit/d4618e49495ace7a6781b06b84b2800407a1e58b))

## 4.2.0 (2025-01-10)

Full Changelog: [v4.1.0...v4.2.0](https://github.com/DataMini/asktable-python/compare/v4.1.0...v4.2.0)

### Features

* **api:** api update ([#125](https://github.com/DataMini/asktable-python/issues/125)) ([af326ae](https://github.com/DataMini/asktable-python/commit/af326aec48e92faebe3cec2f5fbe20d9437c403e))
* **api:** create message ([#122](https://github.com/DataMini/asktable-python/issues/122)) ([e5051af](https://github.com/DataMini/asktable-python/commit/e5051afcfbd84ea53af26b50d617dfa7cab8b22a))


### Chores

* **internal:** codegen related update ([#124](https://github.com/DataMini/asktable-python/issues/124)) ([73e95d0](https://github.com/DataMini/asktable-python/commit/73e95d0fec85b50ed9396038c87084cdba7d19ca))

## 4.1.0 (2025-01-09)

Full Changelog: [v4.0.0...v4.1.0](https://github.com/DataMini/asktable-python/compare/v4.0.0...v4.1.0)

### Features

* Update datasources.py ([bdb8ad1](https://github.com/DataMini/asktable-python/commit/bdb8ad1deb4fe8d9cd6ee16fa2cebb4c6db922ce))

## 4.0.0 (2025-01-09)

Full Changelog: [v3.14.0...v4.0.0](https://github.com/DataMini/asktable-python/compare/v3.14.0...v4.0.0)

### ⚠ BREAKING CHANGES

* **api:** better support union schemas with common properties ([#116](https://github.com/DataMini/asktable-python/issues/116))

### Features

* **api:** api update ([#117](https://github.com/DataMini/asktable-python/issues/117)) ([08bb9e3](https://github.com/DataMini/asktable-python/commit/08bb9e3eab139c7bdb5b19d0a068080e21dade45))
* **api:** manual updates ([#118](https://github.com/DataMini/asktable-python/issues/118)) ([717bcd7](https://github.com/DataMini/asktable-python/commit/717bcd7ae11017dda379a4f9617f9be0c12f55d1))


### Bug Fixes

* **api:** better support union schemas with common properties ([#116](https://github.com/DataMini/asktable-python/issues/116)) ([dced8d4](https://github.com/DataMini/asktable-python/commit/dced8d4627b4ab2264b1d6786d25ea27abc41f66))


### Chores

* **internal:** codegen related update ([#115](https://github.com/DataMini/asktable-python/issues/115)) ([fbf67b0](https://github.com/DataMini/asktable-python/commit/fbf67b023055838adee929909c610df65027848b))


### Documentation

* fix typos ([#113](https://github.com/DataMini/asktable-python/issues/113)) ([8306d10](https://github.com/DataMini/asktable-python/commit/8306d102df314903bd18f2d8b77c36a7c39f23ec))

## 3.14.0 (2025-01-08)

Full Changelog: [v3.13.0...v3.14.0](https://github.com/DataMini/asktable-python/compare/v3.13.0...v3.14.0)

### Features

* patch create_from_file and add_file_and_update_meta ([92ed0da](https://github.com/DataMini/asktable-python/commit/92ed0da376f897885185fb1075f3d9b2f05e8591))

## 3.13.0 (2025-01-08)

Full Changelog: [v3.12.0...v3.13.0](https://github.com/DataMini/asktable-python/compare/v3.12.0...v3.13.0)

### Features

* **api:** Config update for frei-l/dev ([#106](https://github.com/DataMini/asktable-python/issues/106)) ([65d8b08](https://github.com/DataMini/asktable-python/commit/65d8b08db1483acb19cb7863092dc78a3cceee09))


### Chores

* add missing isclass check ([#104](https://github.com/DataMini/asktable-python/issues/104)) ([10aa4e2](https://github.com/DataMini/asktable-python/commit/10aa4e2574524a5e5efc9b6f77bef9067dae2778))
* **internal:** codegen related update ([#107](https://github.com/DataMini/asktable-python/issues/107)) ([6fc5d90](https://github.com/DataMini/asktable-python/commit/6fc5d9056079a39db002893db247d88942a5da70))

## 3.12.0 (2025-01-06)

Full Changelog: [v3.11.0...v3.12.0](https://github.com/DataMini/asktable-python/compare/v3.11.0...v3.12.0)

### Features

* **api:** api update ([#100](https://github.com/DataMini/asktable-python/issues/100)) ([5a7a7bf](https://github.com/DataMini/asktable-python/commit/5a7a7bff6285237055e2670247e3f0321c032ab3))
* **api:** api update ([#101](https://github.com/DataMini/asktable-python/issues/101)) ([cdea94b](https://github.com/DataMini/asktable-python/commit/cdea94b1bf7ad442748dd20248d63a2b8bb22c69))
* **api:** api update ([#98](https://github.com/DataMini/asktable-python/issues/98)) ([a79bc2e](https://github.com/DataMini/asktable-python/commit/a79bc2e704aa56329424db53dec64c9a6d72c9b2))
* **api:** api update ([#99](https://github.com/DataMini/asktable-python/issues/99)) ([f26d038](https://github.com/DataMini/asktable-python/commit/f26d038fd85281cb46b92cb31fecabe10dda82b8))
* **api:** support file management, prolong timeout ([#102](https://github.com/DataMini/asktable-python/issues/102)) ([c38851f](https://github.com/DataMini/asktable-python/commit/c38851fa9587157c56769a52cf4899e16eb2a3db))


### Chores

* **internal:** codegen related update ([#96](https://github.com/DataMini/asktable-python/issues/96)) ([701403f](https://github.com/DataMini/asktable-python/commit/701403feecbfeccb6a3d507322b9dff89d398ec7))

## 3.11.0 (2024-12-30)

Full Changelog: [v3.10.0...v3.11.0](https://github.com/DataMini/asktable-python/compare/v3.10.0...v3.11.0)

### Features

* **api:** add answers/sqls ([#93](https://github.com/DataMini/asktable-python/issues/93)) ([3748b52](https://github.com/DataMini/asktable-python/commit/3748b526f902c65a59a6f8f15b57f960737fda79))

## 3.10.0 (2024-12-30)

Full Changelog: [v3.9.0...v3.10.0](https://github.com/DataMini/asktable-python/compare/v3.9.0...v3.10.0)

### Features

* **api:** add get project ([#91](https://github.com/DataMini/asktable-python/issues/91)) ([8f31c2b](https://github.com/DataMini/asktable-python/commit/8f31c2b29e9074c83b85f17842521d1912d31f05))
* **api:** api update ([#89](https://github.com/DataMini/asktable-python/issues/89)) ([0d63abb](https://github.com/DataMini/asktable-python/commit/0d63abb1dcc253709181d98ac542d9c274020702))

## 3.9.0 (2024-12-29)

Full Changelog: [v3.8.0...v3.9.0](https://github.com/DataMini/asktable-python/compare/v3.8.0...v3.9.0)

### Features

* **api:** add model groups ([#87](https://github.com/DataMini/asktable-python/issues/87)) ([c3aee20](https://github.com/DataMini/asktable-python/commit/c3aee2011aec41dee09a00184844315638ad6b9d))
* **api:** api update ([#81](https://github.com/DataMini/asktable-python/issues/81)) ([60bc504](https://github.com/DataMini/asktable-python/commit/60bc504c4e9ed57580b789306ebf27dc338084ff))
* **api:** api update ([#86](https://github.com/DataMini/asktable-python/issues/86)) ([07ca394](https://github.com/DataMini/asktable-python/commit/07ca394da227e2b3bab90d97e4133db56c4b1675))


### Chores

* **internal:** codegen related update ([#83](https://github.com/DataMini/asktable-python/issues/83)) ([b0e0f6f](https://github.com/DataMini/asktable-python/commit/b0e0f6f3c3bb393985b59735423ae57fa6c986b0))
* **internal:** codegen related update ([#84](https://github.com/DataMini/asktable-python/issues/84)) ([1734cd8](https://github.com/DataMini/asktable-python/commit/1734cd83b34b8e33af03d463425ff06be1333955))
* **internal:** fix some typos ([#85](https://github.com/DataMini/asktable-python/issues/85)) ([f6b99d8](https://github.com/DataMini/asktable-python/commit/f6b99d8e501b5bc5e91b4ece711ab5fc17a82b4d))

## 3.8.0 (2024-12-17)

Full Changelog: [v3.7.0...v3.8.0](https://github.com/DataMini/asktable-python/compare/v3.7.0...v3.8.0)

### Features

* **api:** api update ([#76](https://github.com/DataMini/asktable-python/issues/76)) ([22320de](https://github.com/DataMini/asktable-python/commit/22320de5b9feb14f210b75457bbcf5027d64ce0d))


### Chores

* **internal:** codegen related update ([#78](https://github.com/DataMini/asktable-python/issues/78)) ([95a6640](https://github.com/DataMini/asktable-python/commit/95a66408ffbb0df6fc9a02ac9df930e85a70d39c))


### Documentation

* **readme:** example snippet for client context manager ([#79](https://github.com/DataMini/asktable-python/issues/79)) ([88f2c1f](https://github.com/DataMini/asktable-python/commit/88f2c1ff1f5cd8773cbbdc5ca473d78c84b73f35))

## 3.7.0 (2024-12-16)

Full Changelog: [v3.6.0...v3.7.0](https://github.com/DataMini/asktable-python/compare/v3.6.0...v3.7.0)

### Features

* **api:** api update ([#66](https://github.com/DataMini/asktable-python/issues/66)) ([6594f10](https://github.com/DataMini/asktable-python/commit/6594f1034b276bb3001540d114d02267c1794b6e))
* **api:** api update ([#68](https://github.com/DataMini/asktable-python/issues/68)) ([5fe3dcb](https://github.com/DataMini/asktable-python/commit/5fe3dcb932fd23f19b086540e9fa9153da05760b))
* **api:** api update ([#73](https://github.com/DataMini/asktable-python/issues/73)) ([76b3810](https://github.com/DataMini/asktable-python/commit/76b3810c6f74f12314041abff16e09052f2fa515))
* **api:** manual updates ([#74](https://github.com/DataMini/asktable-python/issues/74)) ([2735ed4](https://github.com/DataMini/asktable-python/commit/2735ed4040e9b0d9adc0b46bc6cd9330269b8787))


### Chores

* **internal:** add support for TypeAliasType ([#70](https://github.com/DataMini/asktable-python/issues/70)) ([c0046ed](https://github.com/DataMini/asktable-python/commit/c0046ed398c750087a03659a92a10240e32d0829))
* **internal:** bump pyright ([#69](https://github.com/DataMini/asktable-python/issues/69)) ([3bd5327](https://github.com/DataMini/asktable-python/commit/3bd5327773c10649284d0e95c55d9ba4a06c0ee4))
* **internal:** codegen related update ([#71](https://github.com/DataMini/asktable-python/issues/71)) ([ef36085](https://github.com/DataMini/asktable-python/commit/ef3608545a5e58e405226176a907dab1b73fc9fd))
* **internal:** codegen related update ([#72](https://github.com/DataMini/asktable-python/issues/72)) ([6a363c3](https://github.com/DataMini/asktable-python/commit/6a363c3cf0964cf648422dd06a13fb4fa7d98808))

## 3.6.0 (2024-12-10)

Full Changelog: [v3.5.0...v3.6.0](https://github.com/DataMini/asktable-python/compare/v3.5.0...v3.6.0)

### Features

* **api:** api update ([#56](https://github.com/DataMini/asktable-python/issues/56)) ([85f14bf](https://github.com/DataMini/asktable-python/commit/85f14bf4c1a6ab1847ea70a1f92ab9fc6b84792d))
* **api:** api update ([#58](https://github.com/DataMini/asktable-python/issues/58)) ([d8e87aa](https://github.com/DataMini/asktable-python/commit/d8e87aa6f7882c7c30c25876c9cd97b975108487))
* **api:** api update ([#60](https://github.com/DataMini/asktable-python/issues/60)) ([d2fde2c](https://github.com/DataMini/asktable-python/commit/d2fde2c2c9dce66f76a81110ece132d64d7e91df))
* **api:** api update ([#61](https://github.com/DataMini/asktable-python/issues/61)) ([b2a2931](https://github.com/DataMini/asktable-python/commit/b2a2931c8ff148f7c9289e5f3a26e212f0a00b6a))
* **api:** api update ([#62](https://github.com/DataMini/asktable-python/issues/62)) ([9a0ade8](https://github.com/DataMini/asktable-python/commit/9a0ade84afdd1533abe882ddff731b7e62dfe949))


### Bug Fixes

* **client:** compat with new httpx 0.28.0 release ([#55](https://github.com/DataMini/asktable-python/issues/55)) ([9b90d53](https://github.com/DataMini/asktable-python/commit/9b90d53934ef35395dd9760e0440cf97e6e0c148))


### Chores

* **internal:** bump pydantic dependency ([#63](https://github.com/DataMini/asktable-python/issues/63)) ([73e26c6](https://github.com/DataMini/asktable-python/commit/73e26c6a80a0a77afaa0a7592f255a2505ac2dcf))
* **internal:** bump pyright ([#57](https://github.com/DataMini/asktable-python/issues/57)) ([a4d4a4c](https://github.com/DataMini/asktable-python/commit/a4d4a4c6a4e9c0bc6f84eccd33ffba754f90a6e5))
* **internal:** codegen related update ([#52](https://github.com/DataMini/asktable-python/issues/52)) ([5ca5165](https://github.com/DataMini/asktable-python/commit/5ca5165218fbe650f9ce1d4dc27cbc2b258c5b62))
* **internal:** codegen related update ([#64](https://github.com/DataMini/asktable-python/issues/64)) ([aa903ed](https://github.com/DataMini/asktable-python/commit/aa903ede9be8e28ba1c2f05cda4455940627f630))
* **internal:** exclude mypy from running on tests ([#54](https://github.com/DataMini/asktable-python/issues/54)) ([3e6ef7b](https://github.com/DataMini/asktable-python/commit/3e6ef7bdd00bd2af75f762c5002d754b314fdf99))
* make the `Omit` type public ([#59](https://github.com/DataMini/asktable-python/issues/59)) ([ebaba2d](https://github.com/DataMini/asktable-python/commit/ebaba2d5e62fad4fa7091436b5713d1096620090))

## 3.5.0 (2024-11-25)

Full Changelog: [v3.4.0...v3.5.0](https://github.com/DataMini/asktable-python/compare/v3.4.0...v3.5.0)

### Features

* **api:** model groups ([#49](https://github.com/DataMini/asktable-python/issues/49)) ([d6695c3](https://github.com/DataMini/asktable-python/commit/d6695c35cb207c7db16eac94ecc2e927a7eebb80))

## 3.4.0 (2024-11-24)

Full Changelog: [v3.3.0...v3.4.0](https://github.com/DataMini/asktable-python/compare/v3.3.0...v3.4.0)

### Features

* **api:** api update ([#46](https://github.com/DataMini/asktable-python/issues/46)) ([328bd3d](https://github.com/DataMini/asktable-python/commit/328bd3d8c4cc07718f3acacb22541eedf97b4a7c))

## 3.3.0 (2024-11-24)

Full Changelog: [v3.2.0...v3.3.0](https://github.com/DataMini/asktable-python/compare/v3.2.0...v3.3.0)

### Features

* **api:** api update ([#31](https://github.com/DataMini/asktable-python/issues/31)) ([268e767](https://github.com/DataMini/asktable-python/commit/268e7672c52e944ce5b86bfb463417ae469b8d03))
* **api:** api update ([#33](https://github.com/DataMini/asktable-python/issues/33)) ([5a4660f](https://github.com/DataMini/asktable-python/commit/5a4660f423deb1ec5edf2a30d44153e00e0771be))
* **api:** api update ([#34](https://github.com/DataMini/asktable-python/issues/34)) ([5db3b77](https://github.com/DataMini/asktable-python/commit/5db3b773117673385135f57c382531417ad72704))
* **api:** api update ([#35](https://github.com/DataMini/asktable-python/issues/35)) ([3d90aa2](https://github.com/DataMini/asktable-python/commit/3d90aa24c6b9312433627ded99833dae3fac32d7))
* **api:** api update ([#36](https://github.com/DataMini/asktable-python/issues/36)) ([9433649](https://github.com/DataMini/asktable-python/commit/943364966023a54ae6a022a8da5b818f0617e3ee))
* **api:** api update ([#39](https://github.com/DataMini/asktable-python/issues/39)) ([0e888dd](https://github.com/DataMini/asktable-python/commit/0e888dd2fcc907d7bb48d7a8cdcf0054063b2f28))
* **api:** api update ([#40](https://github.com/DataMini/asktable-python/issues/40)) ([7d4f6fb](https://github.com/DataMini/asktable-python/commit/7d4f6fbc4ffa228a0a3a9faa2cda71c73cb6aa67))
* **api:** api update ([#41](https://github.com/DataMini/asktable-python/issues/41)) ([95f8c27](https://github.com/DataMini/asktable-python/commit/95f8c270621f46c785261b7ef2356aa326b11905))
* **api:** api update ([#42](https://github.com/DataMini/asktable-python/issues/42)) ([1e6ad9f](https://github.com/DataMini/asktable-python/commit/1e6ad9fa9fee86eb869a88a6a7457b10a321b1dd))
* **api:** manual updates ([#43](https://github.com/DataMini/asktable-python/issues/43)) ([f58065b](https://github.com/DataMini/asktable-python/commit/f58065b10b0af77e5761d0e7bfc6120a5a33ab9b))
* **api:** manual updates ([#44](https://github.com/DataMini/asktable-python/issues/44)) ([8e6183c](https://github.com/DataMini/asktable-python/commit/8e6183c1d338f7a2fe0179f190503ee0fdc520d1))


### Chores

* rebuild project due to codegen change ([#37](https://github.com/DataMini/asktable-python/issues/37)) ([3da94d2](https://github.com/DataMini/asktable-python/commit/3da94d2c69fc812bec6b5ef0dc5f934ba58e706e))
* rebuild project due to codegen change ([#38](https://github.com/DataMini/asktable-python/issues/38)) ([34b494d](https://github.com/DataMini/asktable-python/commit/34b494d2398512da5a44cc6ae6e13a54d324247c))

## 3.2.0 (2024-11-12)

Full Changelog: [v3.1.0...v3.2.0](https://github.com/DataMini/asktable-python/compare/v3.1.0...v3.2.0)

### Features

* **api:** api update ([#15](https://github.com/DataMini/asktable-python/issues/15)) ([0bd4771](https://github.com/DataMini/asktable-python/commit/0bd477131ac8185904589a971e78023c254f88fc))
* **api:** api update ([#17](https://github.com/DataMini/asktable-python/issues/17)) ([6e24354](https://github.com/DataMini/asktable-python/commit/6e24354e23a176d8afccb60c0cc11bb1ebdf33ab))
* **api:** api update ([#18](https://github.com/DataMini/asktable-python/issues/18)) ([8492bb7](https://github.com/DataMini/asktable-python/commit/8492bb7e705d0c60343a272ab7fb5e9cf28d5ecb))
* **api:** api update ([#19](https://github.com/DataMini/asktable-python/issues/19)) ([e9ffbf7](https://github.com/DataMini/asktable-python/commit/e9ffbf7f64390dac45ea2454f06280baab45aa7f))
* **api:** api update ([#20](https://github.com/DataMini/asktable-python/issues/20)) ([eb8d8c1](https://github.com/DataMini/asktable-python/commit/eb8d8c159ec9f6db0cb3400fd28da376a362054f))
* **api:** api update ([#23](https://github.com/DataMini/asktable-python/issues/23)) ([6527b96](https://github.com/DataMini/asktable-python/commit/6527b963f43a6b608283dfaa7f9d90d1140f5fe5))
* **api:** api update ([#24](https://github.com/DataMini/asktable-python/issues/24)) ([83045c6](https://github.com/DataMini/asktable-python/commit/83045c6a90f350182f9c022d74ebb9d3c23f0b59))
* **api:** api update ([#27](https://github.com/DataMini/asktable-python/issues/27)) ([c16037f](https://github.com/DataMini/asktable-python/commit/c16037f8c580a56c5348c82baf04d3f0e1980dff))
* **api:** manual updates ([#28](https://github.com/DataMini/asktable-python/issues/28)) ([a75217e](https://github.com/DataMini/asktable-python/commit/a75217ea3d433687573070480ef7381bd3f2d887))
* **api:** manual updates ([#29](https://github.com/DataMini/asktable-python/issues/29)) ([35884cc](https://github.com/DataMini/asktable-python/commit/35884ccfecaf87c60899ea1a143a8640125d4e8c))


### Chores

* rebuild project due to codegen change ([#21](https://github.com/DataMini/asktable-python/issues/21)) ([911dd76](https://github.com/DataMini/asktable-python/commit/911dd760e7d4022725fcd8607d3c7907d3a7fae3))
* rebuild project due to codegen change ([#22](https://github.com/DataMini/asktable-python/issues/22)) ([9df1755](https://github.com/DataMini/asktable-python/commit/9df175567613a324478980242eee95cacf64a34d))
* rebuild project due to codegen change ([#25](https://github.com/DataMini/asktable-python/issues/25)) ([c5804aa](https://github.com/DataMini/asktable-python/commit/c5804aa3ad70a4470ca30a75460cd12b145fddc4))
* rebuild project due to codegen change ([#26](https://github.com/DataMini/asktable-python/issues/26)) ([6db974f](https://github.com/DataMini/asktable-python/commit/6db974fc42b9933b4ba685d50b08657bdd191747))

## 3.1.0 (2024-10-13)

Full Changelog: [v3.0.0...v3.1.0](https://github.com/DataMini/asktable-python/compare/v3.0.0...v3.1.0)

### Features

* **api:** api update ([#10](https://github.com/DataMini/asktable-python/issues/10)) ([4cbdddc](https://github.com/DataMini/asktable-python/commit/4cbdddc99448537b9bb986ce647ca048ab807413))
* **api:** api update ([#11](https://github.com/DataMini/asktable-python/issues/11)) ([f8e9649](https://github.com/DataMini/asktable-python/commit/f8e9649d2d956ad02735ad67f107576d1d9a7b35))
* **api:** api update ([#12](https://github.com/DataMini/asktable-python/issues/12)) ([8ac4185](https://github.com/DataMini/asktable-python/commit/8ac41859c959e8685213202e85d25b1280fca209))
* **api:** api update ([#13](https://github.com/DataMini/asktable-python/issues/13)) ([c7f3137](https://github.com/DataMini/asktable-python/commit/c7f31371476e5896dcf230b95f7645f2b5fa42d0))
* **api:** api update ([#7](https://github.com/DataMini/asktable-python/issues/7)) ([230366d](https://github.com/DataMini/asktable-python/commit/230366dd4f8c19062e7850df73220a025213e221))
* **api:** api update ([#8](https://github.com/DataMini/asktable-python/issues/8)) ([234cd71](https://github.com/DataMini/asktable-python/commit/234cd71631cb05afac371bc2ad741514d71b15ab))
* **api:** api update ([#9](https://github.com/DataMini/asktable-python/issues/9)) ([0956b01](https://github.com/DataMini/asktable-python/commit/0956b0100295717552c61de84b38900b57b36984))


### Chores

* **internal:** codegen related update ([#4](https://github.com/DataMini/asktable-python/issues/4)) ([df56af1](https://github.com/DataMini/asktable-python/commit/df56af1e43756716339314650602d8cf3b00b781))
* **internal:** codegen related update ([#6](https://github.com/DataMini/asktable-python/issues/6)) ([6403369](https://github.com/DataMini/asktable-python/commit/640336989f2bf2157a6817dccb06a7f030c45346))

## 3.0.0 (2024-09-30)

Full Changelog: [v0.0.1-alpha.0...v3.0.0](https://github.com/DataMini/asktable-python/compare/v0.0.1-alpha.0...v3.0.0)

### Features

* **api:** update via SDK Studio ([c6372e6](https://github.com/DataMini/asktable-python/commit/c6372e622138e1cc69c9155f20ce649098d4f12f))
* **api:** update via SDK Studio ([b06452c](https://github.com/DataMini/asktable-python/commit/b06452cc194222bb6cc2ff2a27c2e50359afde20))
* **api:** update via SDK Studio ([4596400](https://github.com/DataMini/asktable-python/commit/459640081651eb8a96022c94dd3e9ec920349ca9))
* **api:** update via SDK Studio ([c703e2b](https://github.com/DataMini/asktable-python/commit/c703e2b58e25d73fa4e16435962fdcfdcb771969))
* **api:** update via SDK Studio ([41d3520](https://github.com/DataMini/asktable-python/commit/41d352095a1e5a4cc92fe3cac03e915cd3ead80f))
* **api:** update via SDK Studio ([16bb664](https://github.com/DataMini/asktable-python/commit/16bb6645914ae54b1adc45381be8c167b792cba6))
* **api:** update via SDK Studio ([88c4841](https://github.com/DataMini/asktable-python/commit/88c4841c7722a92e5a02353fa2c4e21c7944113d))


### Chores

* go live ([#1](https://github.com/DataMini/asktable-python/issues/1)) ([06e0284](https://github.com/DataMini/asktable-python/commit/06e028455268b73b6d8485dd8a874f604bf50c95))
* **internal:** codegen related update ([066e5fe](https://github.com/DataMini/asktable-python/commit/066e5fe1b28ec2083967303e2d1bbca04165513b))
* **internal:** codegen related update ([71dd372](https://github.com/DataMini/asktable-python/commit/71dd3726e346e841b92173dd7ae11c63accb9385))
