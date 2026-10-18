# Manifes Integritas Hasil Penelitian (Results Manifest)

- **Waktu Pembuatan**: 2026-10-18 13:27:18 UTC
- **Standar Kriptografis**: SHA-256
- **Konfigurasi Parameter (`configs/params.yaml`)**: `cb18e43035028fb98845a23684d6da838a074b9deddd2525edda5725f606cc5e`
- **Keseragaman `config_hash` 360 Run**: Seluruh 360 replikasi di `results/runs/` diverifikasi memiliki `config_hash` identik yang merujuk pada checksum parameter ini.
- **Tujuan**: Menjamin reprodusibilitas penuh dan integritas data hasil penelitian tanpa perubahan tak terdokumentasi.

---

## 1. Berkas Tabel Hasil & Validasi (`results/tables/`)

| Nama Berkas | Ukuran (Bytes) | SHA-256 Checksum | Deskripsi Isi |
| :--- | :---: | :--- | :--- |
| `audit_data.md` | 6,998 | `0b1a76af3b0c17e1c87d1065b3e2001d736c99eecc8ed11a6d20efa01a428960` | Laporan analisis Markdown |
| `audit_data_gaps.csv` | 269 | `ec2832d4d93a2f7efc33552bcc7e996af806044839c24307d230b98175f8d2c0` | Data tabel CSV |
| `baseline_djppr_gross.csv` | 400,439 | `4fc1a5bbcb9c805320cc7d48c0c26218e5324dcae84b8fde605fcef1db56ef63` | Data tabel CSV |
| `baseline_djppr_interest.csv` | 403,352 | `a4f7bf8fe3114d550259292e3a3c600ded1d3b35342319fe7e306065832df7b3` | Data tabel CSV |
| `evaluator_benchmark.md` | 2,176 | `ee102a9fa7811bd23a42dc9a6aa92594d273d5a0ab41fffa4ac7dbfd89cdb096` | Laporan analisis Markdown |
| `gbm_params_table.md` | 6,402 | `ec202d1890254ef091bcdefc93e3da6d93c63ed2850808c40cba6f9c510e0cd5` | Laporan analisis Markdown |
| `limits_and_baseline_summary.md` | 1,922 | `3fea96c7870eed29c33e8c05555deffd311103f9c9d81be697a34b9cd99b78dd` | Laporan analisis Markdown |
| `preprocess_comparison.md` | 4,218 | `22f9f57b171b57af16b09f3094536882d203626be67a3e4da5e6f199150f6fb3` | Laporan analisis Markdown |
| `runs_summary.csv` | 133,054 | `960dd09c8d5be657f1fc0e297a65e5df43326ffdc3d5fcbac5a6ca901b4adcae` | Data tabel CSV |
| `scenario_verification.md` | 3,991 | `25e37facefce51a00dd7df6860aab2377e7f4f5fd69b68d1dbc119e96d5eae87` | Laporan analisis Markdown |
| `stats_dunn_gross_djppr.csv` | 699 | `a9c5bc856d47642c2d92755b47bdc3a0d4e9ee77b0f81f8a793d691257357a53` | Data tabel CSV |
| `stats_dunn_gross_free.csv` | 640 | `008491411b88d71a6849d6652808c992425ee2e89f34ad897825b34b29694d60` | Data tabel CSV |
| `stats_dunn_interest_djppr.csv` | 691 | `820a879634652a8ae9d63e2560f5e33a22fe3fde1cf0af3b5e2b98fad0b1aeff` | Data tabel CSV |
| `stats_dunn_interest_free.csv` | 717 | `257531181ed1798ce354a438819370a0652d5f5238bb4f6b07b5f520050842dd` | Data tabel CSV |
| `stats_gross_djppr.csv` | 1,340 | `489ed0d396ede8cb8721757d75a7d77e288eb95e8d33e4175b043cc2d854cbe6` | Data tabel CSV |
| `stats_gross_free.csv` | 1,350 | `01b988921b0edec30fbb331755415c2adb03cd5f08689604ca61cd39ff46c853` | Data tabel CSV |
| `stats_interest_djppr.csv` | 1,296 | `0e16a0a7cdc29e763c7eceba13e459ac2b8ad0a5ab063001f8663506a7f79652` | Data tabel CSV |
| `stats_interest_free.csv` | 1,367 | `0ac3d480148b38f53fc826cb87283dda69dadb7ee8c268ba25b32826e9d8a985` | Data tabel CSV |
| `stats_summary.md` | 9,697 | `a5f00be2521f4036475bcebb3faa57eeede09ab0d0f5e326ad07f62f8ed02fa5` | Laporan analisis Markdown |
| `tab_experiment_params.tex` | 1,685 | `1a5ff60256e2db8c28fb375b7e96ca8d583a195e67a434a7cbfb124a5f8eb628` | Tabel LaTeX booktabs |
| `tab_market_stats.tex` | 1,376 | `2f29b2eba107d1037c1ad5506cd3a2dd10a0975447b61f26470390d9c3b10f52` | Tabel LaTeX booktabs |
| `tab_results_summary.tex` | 2,164 | `8ab27534caddc7783fb15be4cb4e71a844df6e0d9b71ceafe73b132402d5c415` | Tabel LaTeX booktabs |
| `tab_risk_limits.tex` | 863 | `486feaf4bd879742d74574058a18060c72324488c3728b73a87988eb063f0f11` | Tabel LaTeX booktabs |
| `tab_stats_gross_djppr.tex` | 2,515 | `52eec71b369ec24569949cda86f3dd1555d45852b0ebd2e9c9ab519b8ee6c670` | Tabel LaTeX booktabs |
| `tab_stats_gross_free.tex` | 2,503 | `1166dbf65e35aacadcbf43007bca4c11bfc5572e73329add58901defd77f48bc` | Tabel LaTeX booktabs |
| `tab_stats_interest_djppr.tex` | 2,524 | `426a96f4531a8c93f955fb61c7af8fa0048c11657d55db65f6ca3fbeafc05eae` | Tabel LaTeX booktabs |
| `tab_stats_interest_free.tex` | 2,502 | `219424fb143eda6defa1124c9975be9b464ea96fa639b05896df23db993adcdc` | Tabel LaTeX booktabs |
| `validation_all_runs.csv` | 187,971 | `7f28d4c8b8a2e0172bae913b14c728ccfdb036a26ed83a124942b83517772993` | Data tabel CSV |
| `validation_gross_djppr.csv` | 50,361 | `57bb412cf05a7e29e1d2cd215127b9169718d71956e0cbe1ce65a13fac1852a5` | Data tabel CSV |
| `validation_gross_free.csv` | 42,949 | `8ffd566761ca7d17a861c8ceaf59b15459302d59a5cd8eb6141b60399ef7dfe4` | Data tabel CSV |
| `validation_interest_djppr.csv` | 49,534 | `b500fffae35c1bf2d26c21d4a9d1fb0dec2cf05800f966fe70b8aa0b6e7192cc` | Data tabel CSV |
| `validation_interest_free.csv` | 46,219 | `6734138e82911e4e5e7349226b8e83c443db40ecdfd966aa243c8c07e0dcc49a` | Data tabel CSV |
| `validation_summary.md` | 11,234 | `26ffee59f99e20705d8f67ac9a440e37097f66dc0f974de1d486d17c7192dfc2` | Laporan analisis Markdown |

---

## 2. Berkas Gambar & Visualisasi Ilmiah (`results/figures/`)

| Nama Berkas | Format | Ukuran (Bytes) | SHA-256 Checksum |
| :--- | :---: | :---: | :--- |
| `fig_boxplot_cost.pdf` | PDF Vektor | 49,750 | `3bfb6ebf6692d6c84fe052e3d9bbfc27b30f8c443d5213106ea9be8f3f84712d` |
| `fig_boxplot_cost.png` | PNG 300 dpi | 460,199 | `e3aca7b0ad71980ea80079ea9e9e48c6c6c83596cb5894026983215136c1e3e5` |
| `fig_composition_all.pdf` | PDF Vektor | 82,953 | `3ba514a2e206beda11a58fafc0b542c539d7819a86c85381ea069f439b6779f6` |
| `fig_composition_all.png` | PNG 300 dpi | 604,292 | `37cff036b39a7bd1f6cbba36e0a8cfeb056f22c69643dbf6bca67aef1d5d5468` |
| `fig_composition_gross_djppr.pdf` | PDF Vektor | 78,953 | `15089399239ac6a6f2205ffbfd71d87516b6c0f3172ce35c6b1862beecd163d3` |
| `fig_composition_gross_djppr.png` | PNG 300 dpi | 225,321 | `9018aea34cd53fb8cf95f974220a0ca77eec57d4bb907e4ed7486e160fcc7a48` |
| `fig_composition_gross_free.pdf` | PDF Vektor | 77,200 | `18ece1f6a99057706efe5c1d9ed7aa7dc637453b344df2cff4c7ca8b8748e546` |
| `fig_composition_gross_free.png` | PNG 300 dpi | 214,896 | `705b448a6d0b94d1bc4d35211746df2b7b059f0dbed7b6025bd45411a1b9d197` |
| `fig_composition_interest_djppr.pdf` | PDF Vektor | 78,917 | `8eb12336911e959bd39bf19c8131015a6619ad533dc4b098433b963c16fe476a` |
| `fig_composition_interest_djppr.png` | PNG 300 dpi | 229,847 | `ef8b0cc7a0884b9934d6081ff28247a7010e5f4be8decfea00feefa7f7c0be32` |
| `fig_composition_interest_free.pdf` | PDF Vektor | 77,257 | `24e280f5b3d6017fc4e018946c677729dd437b4f74682204539be6f9cfd8e2c7` |
| `fig_composition_interest_free.png` | PNG 300 dpi | 246,573 | `817e180b5632510d0f67d63dc40476762dfb8fa89241aa548a3b240aa25bdd5c` |
| `fig_computation_time.pdf` | PDF Vektor | 33,435 | `cfa9475d64a45e2bbf0a2af781b7906ea89007144f05dde5e535e63931df133e` |
| `fig_computation_time.png` | PNG 300 dpi | 180,668 | `b28e0b0c62aa66ae777ccb5c0d3b6cdb4d26a726ec810e29fbcb69f3642a1e6b` |
| `fig_convergence_all.pdf` | PDF Vektor | 65,648 | `c1de2373bb629b104c78e6f99c96db0a9cd1901fefd1969aabc261ffb990254b` |
| `fig_convergence_all.png` | PNG 300 dpi | 655,262 | `07236cb86d9988b92b451ba89802ea1a3ce743f76b09a2d7e6940d30aaaf7266` |
| `fig_convergence_gross_djppr.pdf` | PDF Vektor | 46,040 | `6ef698a5b9ff98f0e2c5a2e2bc791c478f1d828f0099ee9d1ea807d98073057b` |
| `fig_convergence_gross_djppr.png` | PNG 300 dpi | 235,745 | `4e6d0bd2fe824d5b4270266154171366fe529b969eb59eb420869a1689df52b6` |
| `fig_convergence_gross_free.pdf` | PDF Vektor | 43,557 | `6ea99f803deb55baeba1fdd2248294d2dda5ed807b65cd6ab6476e483d0c7543` |
| `fig_convergence_gross_free.png` | PNG 300 dpi | 255,233 | `a4dcdb92fed0437c45c84c236461865f78dda3c842b899c3781aa67cf3f1cd81` |
| `fig_convergence_interest_djppr.pdf` | PDF Vektor | 45,627 | `3e4c47ebd7f082a6b21a167d368b5e30df96f15ff82c582d266850b3e4973fa3` |
| `fig_convergence_interest_djppr.png` | PNG 300 dpi | 194,203 | `d39a64d1daae2bdf01ca09d11c5df1cfdf8f6f32d6fb5700ad437169e40164fe` |
| `fig_convergence_interest_free.pdf` | PDF Vektor | 43,620 | `0adb95964c9393ce924c2f3a22ea27dace01251a274d48c6e28a4a217666b741` |
| `fig_convergence_interest_free.png` | PNG 300 dpi | 194,549 | `bfd2fcb0bbc445ac32cc888c8682e6980a4bf59d3b3c89e2a2f67c85f536dfd1` |
| `fig_theta_ratio_all.pdf` | PDF Vektor | 44,722 | `2a25f08fde478e2e464bc02726c9b3edbc0ad95d31f75ec3d94652452627f60c` |
| `fig_theta_ratio_all.png` | PNG 300 dpi | 524,355 | `a9132e5882f651d0988b800bd5f355597d5b49ddb6b672c8eca647f3b2e42d1f` |
| `fig_theta_ratio_gross_djppr.pdf` | PDF Vektor | 39,338 | `0c4e96c643c077d97ce493a7c9d73e70148334a6ce3d325a773f67f9b331e554` |
| `fig_theta_ratio_gross_djppr.png` | PNG 300 dpi | 196,469 | `7f3d2eef9120fc6e7de9eb0e4b84cf3d9b061416fc9128c34472979f8951aefb` |
| `fig_theta_ratio_gross_free.pdf` | PDF Vektor | 38,041 | `c074eed5d4d8d8cd1e70f1e87f67f9a0e592e8acdc3f682ed5e06167cc1ea310` |
| `fig_theta_ratio_gross_free.png` | PNG 300 dpi | 183,013 | `d4bb58b7ad028c19d5d035ff28011dde1867e3a89e9f4fba4dee1cc197fd3835` |
| `fig_theta_ratio_interest_djppr.pdf` | PDF Vektor | 40,553 | `e02bdc92779738913c0c51845c3ec28781ede3b7f5282a12909e9852c454e3be` |
| `fig_theta_ratio_interest_djppr.png` | PNG 300 dpi | 201,844 | `63065502e2e02d06ed8556d3cb2320f3545a87ca11cf4934d5486e537ebf41e9` |
| `fig_theta_ratio_interest_free.pdf` | PDF Vektor | 38,951 | `e24f90bc72e16cd075b0eafb56b8317f43f5e5df28dd529a8d198a49860f2b4f` |
| `fig_theta_ratio_interest_free.png` | PNG 300 dpi | 193,013 | `0cee12a73118a9603d8efddfdcf12d3e6ba272c1c14284115fd12b003edae311` |
| `fig_timeseries_market.pdf` | PDF Vektor | 173,178 | `f3bb69631c4362127598c6c487b7f7a49d935c864e4bb4021b84a300d22c5056` |
| `fig_timeseries_market.png` | PNG 300 dpi | 891,271 | `046d0f9d7e45514f681104565db00e37740b55a0444aee0deaaf94ba9f7b3ff3` |
| `pilot_convergence_gross_djppr.png` | PNG 300 dpi | 217,863 | `97838e51001af6a76051bd24ec52cd73ad1681a4977ad01c7728d5078307e974` |

---

## 3. Log Replikasi Eksperimen Penuh (`results/runs/` — 360 Run)

Setiap kombinasi konfigurasi $\times$ algoritma memuat **30 replikasi independen** dengan seed generator `100` s.d. `129` dan anggaran 25.000 evaluasi.

| Konfigurasi | Algoritma | Replikasi | Rentang Seed | Total Berkas JSON | Status Kelayakan | Ringkasan Hash Gabungan (Merkle Root) |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `gross_free` | `KMA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `38d57b539e8a3ae24499b76344613060896a6f6b162e6858dc6abce62432cac7` |
| `gross_free` | `GA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `edcbbaced7855a67dce7aba3fe7c9413278e0950b1a63835cae1c86e1a030fa9` |
| `gross_free` | `PSO` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `27a61f9fa59031c67c85c041f23f5c07b73d0dbab94081bb2c0352121c07eabe` |
| `gross_djppr` | `KMA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `ca74d708e08b8d1e80262fec8118cd0778ca489fae416dda1582eacd960d010c` |
| `gross_djppr` | `GA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `8ea1661bfc48828d72f3d41ff2be0070c201a67b46aa84bd813b8bf02de9591e` |
| `gross_djppr` | `PSO` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `5202df78d06d1fc8b1f6058cc8d22d3a793a2a5ad31581cffbf3102d4a4b213a` |
| `interest_free` | `KMA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `8ffa0355492da178e756e451ff28da08e363bb1fe0333f8e897694aefdd3828a` |
| `interest_free` | `GA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `041a1cb1fac33db56a31404971e8320cd960bc0c31ea3473b25ff0934252c9be` |
| `interest_free` | `PSO` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `edaa4924d65f9e83b715fc10b97d16ec84d550d4868c8334aa55350f52977bee` |
| `interest_djppr` | `KMA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `e78e77537f125e778fca4f69246211c5cb3160ffb80b1ce74d9cb76228f6a070` |
| `interest_djppr` | `GA` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `c67504a56f8b0206edc9f32fd466178ab1c625f41bf93369ccae634a834b649c` |
| `interest_djppr` | `PSO` | 30 | 100 -- 129 | 30 | 100% Layak ($v \le 10^{-8}$) | `a387df91630e6b978c3a089bc7544b7a5ea84660243015aa47053d57b7d2477e` |

---

## 4. Daftar Lengkap 360 Berkas JSON Replikasi

<details>
<summary>Klik untuk membuka daftar lengkap 360 berkas replikasi individu beserta nilai SHA-256</summary>

| Konfigurasi | Algoritma | Berkas | Ukuran (Bytes) | SHA-256 Checksum |
| :--- | :--- | :--- | :---: | :--- |
| `gross_free` | `kma` | `rep_01_seed43.json` | 16,718 | `e45c5e1ccd4646c8adb38ca42edc10da6f09765b70db0e4de57f1ca151307d31` |
| `gross_free` | `kma` | `rep_02_seed44.json` | 16,779 | `23436d4e9ca5462a41eb8de040751b69f7323b35ca7002ea185bc0959e711bdb` |
| `gross_free` | `kma` | `rep_03_seed45.json` | 16,618 | `c19f0427a1c1673cd92b894afbe30d40e02de3dfc2b57d30d68926d65573befa` |
| `gross_free` | `kma` | `rep_04_seed46.json` | 16,784 | `0df9c0e7089ac85707825d1771c7f310ed59af3d59073ea52fab778741ab0962` |
| `gross_free` | `kma` | `rep_05_seed47.json` | 16,730 | `e0bbf6499a92421a3fac782e436a6e323d22c01f805bd91a18897ddc846d4c19` |
| `gross_free` | `kma` | `rep_06_seed48.json` | 16,741 | `c5c3ee01c2fab931bcd401442a20ece047e19faa75cf81cdd34eea748716db6e` |
| `gross_free` | `kma` | `rep_07_seed49.json` | 16,716 | `deaeacff9f1ba549580be87ddde453e810ee873f01a32f385fa3577c08cdcc3c` |
| `gross_free` | `kma` | `rep_08_seed50.json` | 16,702 | `8fa11c9a6d93dc3b70cd614c9441247b841e48ec60d032cc7b2160777c86e7f3` |
| `gross_free` | `kma` | `rep_09_seed51.json` | 16,763 | `520407edbc3710f771b33614145608eaa30d325ffe172d53df01411367f575f9` |
| `gross_free` | `kma` | `rep_10_seed52.json` | 16,586 | `f6e1fc4b866eb478e8d8b72a4f8e250cee2ff6c5634aa8b0cec33879331365ec` |
| `gross_free` | `kma` | `rep_11_seed53.json` | 16,693 | `e9adfcc160bc128e55bcc84380fa8c299e483b5ae7e14cb9f83bc6817ba2d5ce` |
| `gross_free` | `kma` | `rep_12_seed54.json` | 16,737 | `5ef75b8279496276f01e437c99e196778878a23b4d8b6d3d7f2cb557f79130fd` |
| `gross_free` | `kma` | `rep_13_seed55.json` | 16,759 | `28ab3a8456b7a9b961f80fef1b6392421423333cdc12bfa451a54de8d1494ff0` |
| `gross_free` | `kma` | `rep_14_seed56.json` | 16,678 | `7841d2308fd51ce178a77c5ee86f47650a7a0bf9ed5fdb4ed537f4b9c7df24f6` |
| `gross_free` | `kma` | `rep_15_seed57.json` | 16,611 | `b14f1a01117dafaeddf71c50de59c5c96558785f84679a4984a4cb464724e356` |
| `gross_free` | `kma` | `rep_16_seed58.json` | 16,703 | `13c01c66dc17dd9a0a2147790f891296dbaa2babc969f466919da027b11dc7c8` |
| `gross_free` | `kma` | `rep_17_seed59.json` | 16,724 | `f63971a814c19fb44fc0a684bfe5882072aba24e1d19436d6aaae696ac7e2775` |
| `gross_free` | `kma` | `rep_18_seed60.json` | 16,559 | `5aff642c9922cedca50cfe8ea008d1b3ca5043acf753bde288d8a988b852b010` |
| `gross_free` | `kma` | `rep_19_seed61.json` | 16,609 | `71be07464f08db28f98fdd0e952590feb4a3871212407f6bea306e4115645141` |
| `gross_free` | `kma` | `rep_20_seed62.json` | 16,722 | `8ffce0cc6171e5f7779e8a4c075582a222ffb466401bb0dbd07fb679eb633a98` |
| `gross_free` | `kma` | `rep_21_seed63.json` | 16,713 | `2a4559c527c5fc2301a3a5bdec915c5c71110592a2fea72c6bd97534e8c95f28` |
| `gross_free` | `kma` | `rep_22_seed64.json` | 16,644 | `e9df13b8162c99929413648a6aa2550d952b8fa0710413320d0e4de3742051a8` |
| `gross_free` | `kma` | `rep_23_seed65.json` | 16,733 | `361094eca9ed12d04bfcad6bea5a3efcee9529b205b19622b48b6f792e73439b` |
| `gross_free` | `kma` | `rep_24_seed66.json` | 16,658 | `67aeda6806eed41b9954c4c86326aa1a5cb5be219245f5b5f92208993ef23c3c` |
| `gross_free` | `kma` | `rep_25_seed67.json` | 16,676 | `e2ca6eb18c8af99d96b009745ded8e3eabcbd8cd72f0fd4208be1d91f2644afa` |
| `gross_free` | `kma` | `rep_26_seed68.json` | 16,746 | `3a864457cb03061609a4a87e0d25bf0b6365f1679bf7f778841baa77afd57f20` |
| `gross_free` | `kma` | `rep_27_seed69.json` | 16,678 | `0cedb0a7443a5e3b971f363460afa2fd135941e9ff6b3396bb2b5d81c2f8ef0b` |
| `gross_free` | `kma` | `rep_28_seed70.json` | 16,736 | `7776bbe331d9d336efcc73a524638c688a29c6807c1e1cbd5dd1159a5f2986bb` |
| `gross_free` | `kma` | `rep_29_seed71.json` | 16,750 | `dc30e3009ff7a292643938b18f9a3e66cc90c80200de601acdf3bf0a5185d25b` |
| `gross_free` | `kma` | `rep_30_seed72.json` | 16,694 | `5897aa142b6ddb179edcd394ca02bd31022aefb87c11aaa33e4176b0897e9756` |
| `gross_free` | `ga` | `rep_01_seed43.json` | 16,653 | `1954875d0d4204b31f699bcbb4a00ff2520774c9ca35e07cb57c73b5cb101029` |
| `gross_free` | `ga` | `rep_02_seed44.json` | 16,698 | `79f4899fa3f8a19ff33d455bac5b8401c02585a4203f85692a53f98156a4e09f` |
| `gross_free` | `ga` | `rep_03_seed45.json` | 16,678 | `17a6e2602a51ccf37274becac291f7cf0dd8bef6bb1925052de0a5848812930c` |
| `gross_free` | `ga` | `rep_04_seed46.json` | 16,689 | `9fe6979afbf3bd45c0d4069b15bf51d05169c46e228d1c7cc258764201a15ab7` |
| `gross_free` | `ga` | `rep_05_seed47.json` | 16,620 | `2880feba9780aca9a7f6fffe1a9d8466f3a6278fd6221526c3bca62b69fadd56` |
| `gross_free` | `ga` | `rep_06_seed48.json` | 16,712 | `21dd49f4368554c7d7dc9d1a0ace38478dbb3c6bbeeba2059bb10d2fac7aa7f2` |
| `gross_free` | `ga` | `rep_07_seed49.json` | 16,645 | `24e0162da4c87e9eb6d2fec8222a2ee6b8d9bd26e5f455389f638635d6b653e9` |
| `gross_free` | `ga` | `rep_08_seed50.json` | 16,695 | `dda1ae57278efda4f7d5cc0f99c9f949e8f2d43751d193761db5fccccb13e674` |
| `gross_free` | `ga` | `rep_09_seed51.json` | 16,646 | `2d957d59b41f719eede6022b0940869c1fbe20877a8ae2add83eb030e76335e4` |
| `gross_free` | `ga` | `rep_10_seed52.json` | 16,707 | `86faaade44739897ced0fabe0b5e495877049c6a9f26214820d3857d58c92376` |
| `gross_free` | `ga` | `rep_11_seed53.json` | 16,665 | `186f96c44b1471d75d6b7cee0308f07e72784abbeb183dfe36f0a12865be0703` |
| `gross_free` | `ga` | `rep_12_seed54.json` | 16,669 | `06be267d326d1771e8e68c74a5d2edbec9667f1c317b23d43c02f77d95ebad57` |
| `gross_free` | `ga` | `rep_13_seed55.json` | 16,706 | `54b6e27f0df7edd4825a588595b5d705dd330967b7f1da63a3d62c398fe9aa0c` |
| `gross_free` | `ga` | `rep_14_seed56.json` | 16,703 | `89ec80f38741c1517a6334e7b3ceee90d035c9b43a7d96fd14a6c4a00d515316` |
| `gross_free` | `ga` | `rep_15_seed57.json` | 16,655 | `68f52ceb85bda9de3ddfd41e37bec47506068bd23372a0f104d182b839ecd333` |
| `gross_free` | `ga` | `rep_16_seed58.json` | 16,718 | `aa27288d8887b4987cba3bd191fa962f42ee136b409faa601424f0c1c2be87d3` |
| `gross_free` | `ga` | `rep_17_seed59.json` | 16,708 | `c1531a403e7d2a0d654f1a26f4777248a4b6b6cac8d0f8051f1f206c525fa076` |
| `gross_free` | `ga` | `rep_18_seed60.json` | 16,627 | `2218760d77c8059c47d9341c68af5edd58074f41a47881da2ffe55c47c71a6e6` |
| `gross_free` | `ga` | `rep_19_seed61.json` | 16,683 | `52fc54310560d19969788f39819c78f672890a5430937ce8000705b5b39b93e1` |
| `gross_free` | `ga` | `rep_20_seed62.json` | 16,743 | `2a77fd94b784f17bc88b2edf1a10d7f2a3a824ae319205f7e4ae5b0f42269d00` |
| `gross_free` | `ga` | `rep_21_seed63.json` | 16,581 | `c2b9ad042e932718ffc2f9b005d784ec3e7f5801d5fdaf0f59673549138599e5` |
| `gross_free` | `ga` | `rep_22_seed64.json` | 16,708 | `ea9d444bcb75ec7b82e4f3ee5520fbffd68ebf8f12a4b9e57072c87e57463279` |
| `gross_free` | `ga` | `rep_23_seed65.json` | 16,632 | `09a79b6cc5deae6712fdc0a9e37af8f5933d553e7ba3c02f67a72e70d192935f` |
| `gross_free` | `ga` | `rep_24_seed66.json` | 16,639 | `88959abe8b348e300139e92bf08f96d1f6f6cbf9c4f64120b324abe72a43afb8` |
| `gross_free` | `ga` | `rep_25_seed67.json` | 16,694 | `5d12fe6e7fd9c45fc2cafc21992975929abdace8b3aa4b8024a12ecac63b735b` |
| `gross_free` | `ga` | `rep_26_seed68.json` | 16,634 | `1f5e8b2dd530de09232ac98d3cf366f913db914bdd249f75427616cce5dab453` |
| `gross_free` | `ga` | `rep_27_seed69.json` | 16,677 | `db0e7b888ebcb3522ba4b8e829e43c6c497b0a015291fdef7ba31d275ba07427` |
| `gross_free` | `ga` | `rep_28_seed70.json` | 16,722 | `59e7af5ac5d22c6870e0cd5e6f86bc4fbc4a781fab0f694bfbe14b20a8fd215a` |
| `gross_free` | `ga` | `rep_29_seed71.json` | 16,701 | `3bce041c53deda6c475a6db3e501bbed18a760024335cea80f3f9841eeb6c14f` |
| `gross_free` | `ga` | `rep_30_seed72.json` | 16,697 | `d2fa631a5bcdfaff4ce56e31a4060226ded5afafd5f49a00cd58b3e7b713f191` |
| `gross_free` | `pso` | `rep_01_seed43.json` | 16,702 | `84e5c4559bd095612dd510127a548aa58f277c56197c93ce46a137dc38e567a5` |
| `gross_free` | `pso` | `rep_02_seed44.json` | 16,650 | `0106a4eb7ea7980c9f570391c5d26b68c0ead33d1bfe148919e47ead57d1b3bd` |
| `gross_free` | `pso` | `rep_03_seed45.json` | 16,696 | `31494859c1b203c5046213eb524dfaf49ac99cf0559f1486880a5c0c23ab7d23` |
| `gross_free` | `pso` | `rep_04_seed46.json` | 16,693 | `ffc27e33ae0d28f3d23fdd6af802c704734af036e7dea3ff5bf9491598231601` |
| `gross_free` | `pso` | `rep_05_seed47.json` | 16,684 | `8776c0ef55d4ae94dbe978a762eda90f611212774dc88c305f7ba5aa3acc6987` |
| `gross_free` | `pso` | `rep_06_seed48.json` | 16,696 | `e683f71479dcd8ceb19f37e20bb1d3854d85484c34d25d90dde38fff3225cc9b` |
| `gross_free` | `pso` | `rep_07_seed49.json` | 16,680 | `cbd26c137ed517f8ca5b6c9d0fd8b2dc0b5d6a2582a3a2e7578d95e24ed05839` |
| `gross_free` | `pso` | `rep_08_seed50.json` | 16,642 | `e177263d2fb4308b667085a501a7967da4963671cc16201e2283e3718da412d7` |
| `gross_free` | `pso` | `rep_09_seed51.json` | 16,696 | `23d6b54f094949d6d9a86aa71c99ca08d4e5d10ef7f7ce17da1e8dabddf9e0ae` |
| `gross_free` | `pso` | `rep_10_seed52.json` | 16,699 | `cc886c2cc6ae25a7e5ae9faf78bfd3a65878dfd2209f4e0f18870a479b95ffd9` |
| `gross_free` | `pso` | `rep_11_seed53.json` | 16,703 | `844cdd16ed907513a1bc97a43c7e6c82dafdf6bab2164e1a65727d5f9c9e947d` |
| `gross_free` | `pso` | `rep_12_seed54.json` | 16,700 | `22cf4dd0d47c4d44b473d54bc3d0a6a17b94405f5f145e8b6e4d1bda778e9006` |
| `gross_free` | `pso` | `rep_13_seed55.json` | 16,714 | `33b5dfff5ff2c02f9a58340394922d391688c5d75bceec90015af0278956a9c0` |
| `gross_free` | `pso` | `rep_14_seed56.json` | 16,704 | `6cc8c902b5d2c85cfdeb2f62077f05508ea07e7ad7066fa8b944991c68c39e96` |
| `gross_free` | `pso` | `rep_15_seed57.json` | 16,684 | `e305fb6988f391308b3232dc93be15aadce5300c19359ee04cffa8ef5272d864` |
| `gross_free` | `pso` | `rep_16_seed58.json` | 16,581 | `4ad54b17f61f2811895b411ff887649955731fb74b719bc6156af6000743ff75` |
| `gross_free` | `pso` | `rep_17_seed59.json` | 16,711 | `2ab099fbb4b3b110500edee10c40411d3ae2bb62490dbdbc6bce0027f16f0a64` |
| `gross_free` | `pso` | `rep_18_seed60.json` | 16,693 | `15fa6f3f0c8b79c8ebc312a3313cf34f09aeafb102217128249ea13dcc89335e` |
| `gross_free` | `pso` | `rep_19_seed61.json` | 16,693 | `b1832ace414b32b3c035837785b41c57b9b57e3eeaa3f156d99b899624a7a918` |
| `gross_free` | `pso` | `rep_20_seed62.json` | 16,701 | `6de813ba41047631dc3a30486bde9852aa920412a2f8b750c376293e5003ccae` |
| `gross_free` | `pso` | `rep_21_seed63.json` | 16,641 | `bb2b424748fcbef696a489059242ae9b8feebad8295879090b664fc1fe7070aa` |
| `gross_free` | `pso` | `rep_22_seed64.json` | 16,690 | `0df3d0fa6e60f30aeef59b45b35a5a7b3f5231cc2d46f2183e159673600200bb` |
| `gross_free` | `pso` | `rep_23_seed65.json` | 16,650 | `575fd988fe905d7cd569e0e0b51c016fccb2e28d24073ac9d4bf20ceb9cde46e` |
| `gross_free` | `pso` | `rep_24_seed66.json` | 16,674 | `77f190eb8310bc24e0411aeb4da64fe95cbbaa40b3596b7f2dd028ab60111549` |
| `gross_free` | `pso` | `rep_25_seed67.json` | 16,702 | `e02864e85fb10c9b14ffdd5f0c8eb8ef7b9a9ab1e826e81e5b19509568f11689` |
| `gross_free` | `pso` | `rep_26_seed68.json` | 16,666 | `9b99141dd87d3f61dfd078d7b4349f64b8ad1eece590da4292b5c447a53bb142` |
| `gross_free` | `pso` | `rep_27_seed69.json` | 16,703 | `2938050c4a82f73a24cd81ce4231efcbdc33720da7c38a6bea85f979e28bb625` |
| `gross_free` | `pso` | `rep_28_seed70.json` | 16,638 | `8d9658580de4d553f740f24fe50a1b8e8bf71eba88c716b75c65dd46cf15c914` |
| `gross_free` | `pso` | `rep_29_seed71.json` | 16,711 | `a5cb3bb9d02b1e6bee78418f341d061afdc24ba7b937d4d2e72ce0be67ab3437` |
| `gross_free` | `pso` | `rep_30_seed72.json` | 16,660 | `01822fc66e9e46a6d770c2e7a47d8666f596d21ef5082cd24e6ab31077320137` |
| `gross_djppr` | `kma` | `rep_01_seed43.json` | 16,605 | `a8af8645e427ec2dd80c401a3fcd497f2f77d9e0f992bbc3aa656973694e6d36` |
| `gross_djppr` | `kma` | `rep_02_seed44.json` | 16,757 | `88928f0a25a315b3fb815a4eafd5ea05f3404934f8b081ec64d9aa7315ff90b6` |
| `gross_djppr` | `kma` | `rep_03_seed45.json` | 16,780 | `80cb243746242f3e81c0da20225d03eb8c35dc1fd802342e2553b9bea7a1c921` |
| `gross_djppr` | `kma` | `rep_04_seed46.json` | 16,787 | `b8f78af436c7934affec51aa7fa7be26eaeb0914fe330a4f9087e4ae34441b22` |
| `gross_djppr` | `kma` | `rep_05_seed47.json` | 16,782 | `b63049a451cf886a64a7233a66e665c8c243221519f0bf30f9475fe2ac3b15da` |
| `gross_djppr` | `kma` | `rep_06_seed48.json` | 16,787 | `a6867c83f20babb3ac35d3af71af0450b2a064ae3748b87233c72703ac32bb19` |
| `gross_djppr` | `kma` | `rep_07_seed49.json` | 16,784 | `7866956e1eccc1288320369b74ff85b67036a3d195c03fede1a6b212c59f84f6` |
| `gross_djppr` | `kma` | `rep_08_seed50.json` | 16,715 | `d2d9e724213215e0eb20ec2c45fbb41e123deffcc75888d0b3c1e87f342661be` |
| `gross_djppr` | `kma` | `rep_09_seed51.json` | 16,699 | `8aaa2bf4892d627ca639b72c5a03881dddfc05e3dda1f1379ceb3e0bc5d045fb` |
| `gross_djppr` | `kma` | `rep_10_seed52.json` | 16,780 | `a965e44fe05c9ac703b0df4862c3e3b77dac022bac367398708bc2c44bacbd24` |
| `gross_djppr` | `kma` | `rep_11_seed53.json` | 16,760 | `a1dd5b6155c31121197ad2a6fb8d70c61d01bbc2737a2866df4ffd9818702b46` |
| `gross_djppr` | `kma` | `rep_12_seed54.json` | 16,784 | `049bf0b7f59f1274a821ac0a210be85708e449c64f0e5e17dd603d0d4211aec9` |
| `gross_djppr` | `kma` | `rep_13_seed55.json` | 16,789 | `505121ca3e7a921f1640d1241229adff306eb90b898290f95464403209a3e972` |
| `gross_djppr` | `kma` | `rep_14_seed56.json` | 16,797 | `4c02b068bd0644635130697fe2571a12dd86b4cd0b554a3b39f5e6a8f072bc67` |
| `gross_djppr` | `kma` | `rep_15_seed57.json` | 16,781 | `c12814b8382336798f83f80bd6d69d5e5f95805fa6585575062d1722bcb162c7` |
| `gross_djppr` | `kma` | `rep_16_seed58.json` | 16,746 | `d2261573f388597c517d7c35d114e591aa9ef801a29e49813f0a4f186a2fe5f5` |
| `gross_djppr` | `kma` | `rep_17_seed59.json` | 16,623 | `275140c70ff8ddf3b312203eacf1a9a563245c3338aad09eef3182bf7447ae2f` |
| `gross_djppr` | `kma` | `rep_18_seed60.json` | 16,776 | `c44b4184b06f48922d802149d4a120a540f881eceb622ae494f14522778eace2` |
| `gross_djppr` | `kma` | `rep_19_seed61.json` | 16,780 | `96d85bdfbb19e11bb0580124ddbfe581bfcc2b2e5c9d37039bfd5b28aee15202` |
| `gross_djppr` | `kma` | `rep_20_seed62.json` | 16,783 | `e607fc5a598a0af7c2bd5c9a5c868e6b01f8af8694225a42968f70bad7dce8d2` |
| `gross_djppr` | `kma` | `rep_21_seed63.json` | 16,795 | `a97fe75a8410dce20aa8b29760c3aba69ad6cacf6e908b8f848c236dd6d1c181` |
| `gross_djppr` | `kma` | `rep_22_seed64.json` | 16,790 | `d77eb6cd14b7583a870566b8ca374dcf9e37f169bbbf4fb46985e396236fa03c` |
| `gross_djppr` | `kma` | `rep_23_seed65.json` | 16,639 | `688cc102bd9de8ac305e7cc799e9dd080fd216aec796e8e2803c1591488db7ac` |
| `gross_djppr` | `kma` | `rep_24_seed66.json` | 16,780 | `9ad5981d513de48e4ffcb0e1e6ab434a198ffe8f047b0e1b361dac84fc9c9734` |
| `gross_djppr` | `kma` | `rep_25_seed67.json` | 16,786 | `5f92a799afe20b852f184a6c8730b381dc59b4fdae0e0a79b1976138464840d2` |
| `gross_djppr` | `kma` | `rep_26_seed68.json` | 16,717 | `9fc04fb300b50cbc7da6b4a28e4a707f205697b83df14d1136fba95b7ca6174b` |
| `gross_djppr` | `kma` | `rep_27_seed69.json` | 16,757 | `17ff12a6bf69a3bfadafe661f9ba223c7fae8f5bae23f6988745cff7aeb36cdd` |
| `gross_djppr` | `kma` | `rep_28_seed70.json` | 16,613 | `9634814951992c4c9438c97adb32ed840d24ebc626327df78ae340599c9ef79f` |
| `gross_djppr` | `kma` | `rep_29_seed71.json` | 16,790 | `d37367adbdd2dda2e3b8bfa687ac65faf131a8c6888d8843153cd439bf2d76bf` |
| `gross_djppr` | `kma` | `rep_30_seed72.json` | 16,795 | `e904357dc73864b53e7ebee8c07094fa01de09c46c1f8c2603d6c052b68a0099` |
| `gross_djppr` | `ga` | `rep_01_seed43.json` | 16,725 | `16bb2cf7f2d3fb501d556aa88e9ec1e6baf810a7528ee2271cbca6410bb2e4e1` |
| `gross_djppr` | `ga` | `rep_02_seed44.json` | 16,754 | `2c69b7a91ce22c3af2cc57720fed3a3031c9fca756b9fd0d78aca009bfe3ebe4` |
| `gross_djppr` | `ga` | `rep_03_seed45.json` | 16,736 | `e52e3406e5e886a455b8887d182e98b778cd6db030f578a1bffdb24a833b9828` |
| `gross_djppr` | `ga` | `rep_04_seed46.json` | 16,764 | `52cb8049b689163e380526dbedd7deec77e1fea02b11a609c700ddc0989ba14d` |
| `gross_djppr` | `ga` | `rep_05_seed47.json` | 16,766 | `57283ed0dc7eda795ffffceb8aaf5ec0270484831b6df4b46cc27b10919a4a78` |
| `gross_djppr` | `ga` | `rep_06_seed48.json` | 16,732 | `8d107a328fb9d0607095a5ab77255708a6555bde1658e6036751b1bb9ba6002e` |
| `gross_djppr` | `ga` | `rep_07_seed49.json` | 16,729 | `4e4b8a26ab7c6a8a9a11f9a796964e6a924b87c7c167b54ec420c2f26bea08f5` |
| `gross_djppr` | `ga` | `rep_08_seed50.json` | 16,760 | `933012a3874613a9fcab04721fac1e0f5909c3671f9cd0c4f75490bdc092d39e` |
| `gross_djppr` | `ga` | `rep_09_seed51.json` | 16,749 | `24eaa0be4828d407ffb2dcbf67e86797d9526101c8b6d20530e67b8499b84515` |
| `gross_djppr` | `ga` | `rep_10_seed52.json` | 16,702 | `0aed7a1db58e14d3d13c86d139f0a8513b0f76dbe6105ea53b1ab26424d562bd` |
| `gross_djppr` | `ga` | `rep_11_seed53.json` | 16,723 | `6e520669dd06231c1a105bb911b5c4f878e55a119bfeebc3141fa32e396fea25` |
| `gross_djppr` | `ga` | `rep_12_seed54.json` | 16,770 | `87d4c0c2f956383dee33e61bfd1c3cc05dc43220e9b3afdba252e574d5fca7fa` |
| `gross_djppr` | `ga` | `rep_13_seed55.json` | 16,764 | `2edada18755e41a0bf449b39d52370ecbf4d55a5607fffedefff9f001e553139` |
| `gross_djppr` | `ga` | `rep_14_seed56.json` | 16,747 | `d4cad590151b8cac31630d0d3baf86b1d3803f53c50111f8b3376cf8414d8573` |
| `gross_djppr` | `ga` | `rep_15_seed57.json` | 16,730 | `16db631c18b57c1508b7e5114b57461f0a82a2e87f94c3a5359415e3c2b668e9` |
| `gross_djppr` | `ga` | `rep_16_seed58.json` | 16,741 | `e8c894d2cc926d1dcd21f384f719430a6f026f8f999fe0322b3be3c3fb312984` |
| `gross_djppr` | `ga` | `rep_17_seed59.json` | 16,759 | `122f80ffe1f510b5a3ab194aac093d42869b6a8eb789d8e68ded804b7e8a8441` |
| `gross_djppr` | `ga` | `rep_18_seed60.json` | 16,763 | `e2a7e25df949cedb1f948724f9c2cd363252b5525aeb26b3b50c7e60a07dc34e` |
| `gross_djppr` | `ga` | `rep_19_seed61.json` | 16,731 | `8a42970cfcacb9f0d518f9766153ab4a51dc3903f15130dc47b485740f7a2a22` |
| `gross_djppr` | `ga` | `rep_20_seed62.json` | 16,758 | `eb58780e6396305fc1d1af3587e0a347f585fd1ba012c7af37524b15102bc6c6` |
| `gross_djppr` | `ga` | `rep_21_seed63.json` | 16,737 | `42d428c4a52c56884fc91c3f0d1400ca064bd63a390f264e01782fd83faa5e58` |
| `gross_djppr` | `ga` | `rep_22_seed64.json` | 16,717 | `bd073bbcbc82e04c99fe120aa7d5a8f80dca8c40a993e712c2b0201b194ab18a` |
| `gross_djppr` | `ga` | `rep_23_seed65.json` | 16,761 | `3f31c7bb283dc28c8081fa055b3623ba15186638685a5ac48dfcf5681bb2b7ef` |
| `gross_djppr` | `ga` | `rep_24_seed66.json` | 16,725 | `f24bba91e5c1f86e67e0eab124f73aec848362b3f380218ffbccef84c24f0d24` |
| `gross_djppr` | `ga` | `rep_25_seed67.json` | 16,750 | `29ac3560622bb6e8adae1317a690761a3d970b29da7fe8060d4785815e11ac2c` |
| `gross_djppr` | `ga` | `rep_26_seed68.json` | 16,749 | `b6376e916196399cba962541836b0a8143ebeefea3112d2c125d00705530a8ee` |
| `gross_djppr` | `ga` | `rep_27_seed69.json` | 16,771 | `721083d6d0831a6acb5fcb2bac86305860300f6f84120a1db45e3e20ca142a7c` |
| `gross_djppr` | `ga` | `rep_28_seed70.json` | 16,783 | `34ef06ca1fffe23cc3ddf744bcc6917e560ba5e65539b197286f91eafbed3458` |
| `gross_djppr` | `ga` | `rep_29_seed71.json` | 16,745 | `c27bbb524973512e18ab2389649041171f810c841bfd3751cd145d7bd530cf21` |
| `gross_djppr` | `ga` | `rep_30_seed72.json` | 16,721 | `db7b8e109079d013b247462baa80d848733401e50b510f42d3f62325806cd6c6` |
| `gross_djppr` | `pso` | `rep_01_seed43.json` | 16,723 | `30b62401bc6024294254de346a6f0433aa9097ffaf5928a26e19495f92b4c1f0` |
| `gross_djppr` | `pso` | `rep_02_seed44.json` | 16,756 | `2638546b1375ba6f2824e1c3ef326b5c3cf32e071bc96682b1f6f67da46bb020` |
| `gross_djppr` | `pso` | `rep_03_seed45.json` | 16,736 | `92ee3fe81236439035832f47217b92db49bae54c76966c5887ce60b11994c4ab` |
| `gross_djppr` | `pso` | `rep_04_seed46.json` | 16,751 | `be0e4e960d8a523e79a198c8b59ce357edd913a10876970ec6e058f701210cb1` |
| `gross_djppr` | `pso` | `rep_05_seed47.json` | 16,749 | `a5892ee5121c41dd5ebbc30729993690cf12e33d77cc35f2a8081ce8ed12921b` |
| `gross_djppr` | `pso` | `rep_06_seed48.json` | 16,715 | `3ef9473b17107a2bab8a9ced1b56a8e27df9adffbd5a57f79cd637dcbefad83f` |
| `gross_djppr` | `pso` | `rep_07_seed49.json` | 16,757 | `f379156d20923807527fe56f500778608ca5a345d269e33216a22955ff4db262` |
| `gross_djppr` | `pso` | `rep_08_seed50.json` | 16,745 | `dc4e7b5a363c798f1ac3ee684cd084b1ff183d7d08c1ae432f3d2e3976cf9f1e` |
| `gross_djppr` | `pso` | `rep_09_seed51.json` | 16,768 | `cda9d0f67543ef974221ad3589f7ace6b528bee2e809762b3bd94150fb297936` |
| `gross_djppr` | `pso` | `rep_10_seed52.json` | 16,763 | `16e022bfaa880f96af452982645a94a1d64b934df6d27225674c5fca90515b8a` |
| `gross_djppr` | `pso` | `rep_11_seed53.json` | 16,757 | `3e5a244b0eaf856baad370454549aedb4f9435679e7f5d8764a4ac7ee167ff1b` |
| `gross_djppr` | `pso` | `rep_12_seed54.json` | 16,765 | `9934ff36123e1a6f9096560a742b44fb2e6e6ae435b6733da0b5d99c1d4f2edc` |
| `gross_djppr` | `pso` | `rep_13_seed55.json` | 16,763 | `837eac008c2ef01ad6c20853ee80552fc78103ae7218a6e47487337bc96f4e42` |
| `gross_djppr` | `pso` | `rep_14_seed56.json` | 16,760 | `2e2f7172809be56ead303529f39052820770cc2c0478a8d4bfca92e28dd67c4b` |
| `gross_djppr` | `pso` | `rep_15_seed57.json` | 16,761 | `df9ce3182e444f8099694a398f08fe867915f3b75455ed2ad6d6606c96fadeb1` |
| `gross_djppr` | `pso` | `rep_16_seed58.json` | 16,762 | `69d4f707ab326d86e61030bd9e069a98b3dd83027cb0476ddae38ae5b5a228f3` |
| `gross_djppr` | `pso` | `rep_17_seed59.json` | 16,759 | `6a75479a193c6d1b23eae24139f57be676f0afde3114819181c391abe5b78548` |
| `gross_djppr` | `pso` | `rep_18_seed60.json` | 16,762 | `bd485188fb8e358aff91b9e32525b76dd96b42ae2ea7fecee1c31f3376b6e6ae` |
| `gross_djppr` | `pso` | `rep_19_seed61.json` | 16,760 | `7d8fc49f761450e3cd28bab22f9889069ec4a28d8588e11bd3a5b2d6a25752a7` |
| `gross_djppr` | `pso` | `rep_20_seed62.json` | 16,770 | `a3df229bb78c5dc0faeddba5873b777c03e5691ac989fa667593224c11ed771d` |
| `gross_djppr` | `pso` | `rep_21_seed63.json` | 16,765 | `76f2fa4ee02f1e704374b3439828ec665d8c518840fc00be9ffd1319dcc767c2` |
| `gross_djppr` | `pso` | `rep_22_seed64.json` | 16,766 | `224437e53d007aaed2fdd75d307c50730c8997b2439bd63e64f90a1878bbe9d9` |
| `gross_djppr` | `pso` | `rep_23_seed65.json` | 16,769 | `f65765ab3e4431cb20e6fa51de440d968225468551e8dd39aa2986e77dff8234` |
| `gross_djppr` | `pso` | `rep_24_seed66.json` | 16,721 | `af727553b3374e96812a3595aa9553049926d7e5a5482c8a9353298c6b748b29` |
| `gross_djppr` | `pso` | `rep_25_seed67.json` | 16,777 | `ec46418dde6a73c5944355e8485dd4c03b3050403eaa7f4351a560f89871ba7d` |
| `gross_djppr` | `pso` | `rep_26_seed68.json` | 16,751 | `447223c7e2a971b690c4d4f1fb21511082e00c076e2b3eab04c4b11125749ef3` |
| `gross_djppr` | `pso` | `rep_27_seed69.json` | 16,761 | `25aac5d64d39802acf586d8309e4a88696d287bb0d0ab9bc6d714e00d79d7344` |
| `gross_djppr` | `pso` | `rep_28_seed70.json` | 16,756 | `8e50f6e22c68a24cd624e014472082d07dd9a683df1031e367312d5185f701fc` |
| `gross_djppr` | `pso` | `rep_29_seed71.json` | 16,765 | `6aca148b20f805a287a41f630efdb64391d84b285da64999dc6871c0c6bdfdbe` |
| `gross_djppr` | `pso` | `rep_30_seed72.json` | 16,756 | `3b1192529e9e60e7eb2a53cc437767bc339c29679b6123d8fc7a626a339e26ac` |
| `interest_free` | `kma` | `rep_01_seed43.json` | 16,835 | `64ba6ab1aea53072c2b8a56972dc29e935bfdb53b1f00a0283a4ba6f37826ffc` |
| `interest_free` | `kma` | `rep_02_seed44.json` | 16,826 | `c5c09fe22243b124b4540b31dbdddf6b73054eb629233f2c024fcfa951c12819` |
| `interest_free` | `kma` | `rep_03_seed45.json` | 17,007 | `63a06e9db0f8a2d581436f0c1d385d7b3fb6e2976b979f8b07960c293df60625` |
| `interest_free` | `kma` | `rep_04_seed46.json` | 17,021 | `d606180444be7b8edc99da0a8d268062c1b36426705f65c8807d1abb6218f056` |
| `interest_free` | `kma` | `rep_05_seed47.json` | 17,037 | `77d84aa4e73280918ad4bbd4f08fc817a69c9e08acd4900c99cf539085126d9c` |
| `interest_free` | `kma` | `rep_06_seed48.json` | 17,169 | `95054256607df37bb5737ec86b4f7a131ef6a67bd2463efedd0a81ec351f9a2e` |
| `interest_free` | `kma` | `rep_07_seed49.json` | 17,189 | `78b56cffa40d45c7c9909f3faaf7ad6253067c68bbf37de871ca0e2be128c409` |
| `interest_free` | `kma` | `rep_08_seed50.json` | 17,012 | `542eb639c91533b4101c6244f45889463a2487f0d81382f2afa29dd23eb5ac5d` |
| `interest_free` | `kma` | `rep_09_seed51.json` | 17,059 | `afce0a23866a470a6d3ca6aec8be083eabfce9f020a70221b81833c9f29bc8fc` |
| `interest_free` | `kma` | `rep_10_seed52.json` | 16,932 | `e95f323f2a329219a8cec1e16209940c3946bbc5b7bb3cf8bb4b2bcd83d252e9` |
| `interest_free` | `kma` | `rep_11_seed53.json` | 17,187 | `b5871916b290a01fd008349489d0c1e84d1a8e8bfc1c6709e6fe5825babffb80` |
| `interest_free` | `kma` | `rep_12_seed54.json` | 17,051 | `e1443aac87e03b2e4eae63727e4aa7bbcd1d86d3bd7fc470fe6f1b9e10e11dc0` |
| `interest_free` | `kma` | `rep_13_seed55.json` | 17,080 | `3e91ccecc53c40bb1c3b24abdcc8bfd882b8c593f4d3057363befe757fe799f3` |
| `interest_free` | `kma` | `rep_14_seed56.json` | 17,195 | `28a9771129581c7513cf0943b6ca83285491f3fd785c36f4bf982fd08b447baf` |
| `interest_free` | `kma` | `rep_15_seed57.json` | 16,901 | `b3e65af6e244b1c562c9807c50c3e914fe78e8cb3c164615c189fc49cbcac0da` |
| `interest_free` | `kma` | `rep_16_seed58.json` | 16,884 | `2a72e89617b18303ac8cd6c698d1364863b81446177ce267afb7a6a55e35a1c0` |
| `interest_free` | `kma` | `rep_17_seed59.json` | 17,093 | `0e5000f08df4cfcbd76d8c9451b50754d329063d3e1e5e554e57e0fa62b5b130` |
| `interest_free` | `kma` | `rep_18_seed60.json` | 16,991 | `f5604a3cfbcf3725ed30ca6a660d9477decb4ef571b5ad1ca1aeb34b4d55d8c3` |
| `interest_free` | `kma` | `rep_19_seed61.json` | 16,941 | `cbbd47248855bcf4010eab45dea4e5468dbb3f9b38efca0c5459f691e47ac5a8` |
| `interest_free` | `kma` | `rep_20_seed62.json` | 17,134 | `2cac4ae11f3b7c8fe2d4ba6054fc425ec95a94e85f5068fe07c28c7602c546d0` |
| `interest_free` | `kma` | `rep_21_seed63.json` | 16,966 | `0ddd8ef8948291ff50ee78ecfcf157c898792b4cd8ee317a711b8b68f3335206` |
| `interest_free` | `kma` | `rep_22_seed64.json` | 17,048 | `3365a6ebca33012d01082f9a6f51bb829230608e7a87984654724e496f819604` |
| `interest_free` | `kma` | `rep_23_seed65.json` | 17,223 | `7bcfb1b7402a493e3ceef169a8f97004c2e646f8ffdecd411a94aca4bb33df5a` |
| `interest_free` | `kma` | `rep_24_seed66.json` | 17,005 | `9442afd4da72d7b696adcaf8cda3c8aeaa8c3b57c02e2463863ec0871a472a15` |
| `interest_free` | `kma` | `rep_25_seed67.json` | 17,213 | `c01f88bbb16b4f3fcb50e0a7d171859c49954a50bd0c562920d2664c08bc34f7` |
| `interest_free` | `kma` | `rep_26_seed68.json` | 16,997 | `ac1dcc44ea1875262ff87c677426de360d37765e8178803ecce50522831ec88a` |
| `interest_free` | `kma` | `rep_27_seed69.json` | 16,992 | `c51b620993375b7d05acba072b36c3f64a53fde62923e697ac633e007aefabdd` |
| `interest_free` | `kma` | `rep_28_seed70.json` | 16,979 | `faa6335449aa70eed23683bdbabcf3b338aae01556845e0a5b8516034f896c50` |
| `interest_free` | `kma` | `rep_29_seed71.json` | 17,119 | `bb922d2ef26d6c120986a372aeca2f267bc7fe97deae7662b4ab89b87b40b2f1` |
| `interest_free` | `kma` | `rep_30_seed72.json` | 17,083 | `f02ed386bf9679c01014e76a570060f0b5486356e7e8351936b8d6a255e018fb` |
| `interest_free` | `ga` | `rep_01_seed43.json` | 17,108 | `3aa16b467eef665e44a8ceee20a6eb90fcf31b774a3cadf5c5e1546fdf69e9dc` |
| `interest_free` | `ga` | `rep_02_seed44.json` | 17,118 | `c8ed15a6654001147e207f9c019098fd3f744171a5403f10cb3395aafe914bc7` |
| `interest_free` | `ga` | `rep_03_seed45.json` | 17,100 | `685d7824c9e18d878ec35ff31f97b5b9e40a405ee52e9beb94cde450c9dcd7f7` |
| `interest_free` | `ga` | `rep_04_seed46.json` | 17,113 | `96187ca27e0006cbc18b9a58698c75d3d729375c6ebbf57194e9cbf8cec77b77` |
| `interest_free` | `ga` | `rep_05_seed47.json` | 17,124 | `e0fdbeb2b6bd18936afce5c60351a441db067a2bad66ad874935ba39f4f14d91` |
| `interest_free` | `ga` | `rep_06_seed48.json` | 17,141 | `4efea681080100d3aac84ecc7a3e4b61f8202cdb6579e417e1201c89b1ec65fe` |
| `interest_free` | `ga` | `rep_07_seed49.json` | 17,126 | `81e8fbdce5d2ef0f00a1dc78d19ac59e9a43bbcb2310314db0f5ed7f69020f3a` |
| `interest_free` | `ga` | `rep_08_seed50.json` | 17,136 | `f270fe300c2c414dfa14e8757fb29a39df7acbabece71224ff0329d44927a6b9` |
| `interest_free` | `ga` | `rep_09_seed51.json` | 17,146 | `b90b949765825ce673b9c80c9b3a03e2d43c5bb815e15e74cf49906fdd9a5960` |
| `interest_free` | `ga` | `rep_10_seed52.json` | 17,158 | `cd1da79183470aa92bc4c41a7791f865b8c97635c7d19682c69d90cb4bb6ded1` |
| `interest_free` | `ga` | `rep_11_seed53.json` | 17,136 | `b76e2f05240519cb8128876d234eb6863e2967237f2200457ba9b044bd0f0f26` |
| `interest_free` | `ga` | `rep_12_seed54.json` | 17,049 | `b619728f8178f439a2c2f18636acaab2c9d60e73e269ce0f769d33fff6f8a933` |
| `interest_free` | `ga` | `rep_13_seed55.json` | 16,974 | `767b0de499fc3f01e0421a5f42d64d2e8fc9f459d5b8d4077802d2c64e57b3c9` |
| `interest_free` | `ga` | `rep_14_seed56.json` | 17,175 | `3da6ec29089f11f85d4564c9a0f8cbfe689874a8add2e8dee847df0ad8b05dab` |
| `interest_free` | `ga` | `rep_15_seed57.json` | 17,046 | `d413caa1cda8667493ae325eb8fe7d259b095bd786233c7f02b7ccd309dc508b` |
| `interest_free` | `ga` | `rep_16_seed58.json` | 17,051 | `db203a87c5cdf4050b7b3b1c26e031088e250771173777b07dafc41fc259d1dd` |
| `interest_free` | `ga` | `rep_17_seed59.json` | 17,100 | `fdf6fe3ffc5fee348b7f706ca4b2eb9f24b25ae8036f50d447aaafc146eec534` |
| `interest_free` | `ga` | `rep_18_seed60.json` | 17,123 | `b0911a2b3e6143a9e624dc3d4cb02d9fe5ce3004357f4341f9d670309eb93588` |
| `interest_free` | `ga` | `rep_19_seed61.json` | 17,117 | `e91055c3c0c4c5185f16d734582044e47baca5fcd3f11238f13f999af4a028f1` |
| `interest_free` | `ga` | `rep_20_seed62.json` | 16,933 | `45e925e3d1085a8629e80df7d4124ff17199e3ae3624bfaa31d68e4b271eecbf` |
| `interest_free` | `ga` | `rep_21_seed63.json` | 17,148 | `5a2aecd7c61524d0a56b2b61e5c31631ff5dcd4d6da908c5ac939d2491123ca0` |
| `interest_free` | `ga` | `rep_22_seed64.json` | 17,118 | `fba43e34c794106dcf1131c586d275e6e3a248820a0fafa9ee80fa84355f0165` |
| `interest_free` | `ga` | `rep_23_seed65.json` | 17,157 | `adc8f07361474f7f63659ef4339ecd6f35e42999a78b07926b825f3aa2a6299c` |
| `interest_free` | `ga` | `rep_24_seed66.json` | 17,079 | `68f683d67412946cdc53299446cdc5837e9ba53926456942f2f1efecec72ab93` |
| `interest_free` | `ga` | `rep_25_seed67.json` | 17,124 | `36b7cabacc5b133b9fe2241561b3bafb7e671152f35f8d87e4d464af9b45ce5d` |
| `interest_free` | `ga` | `rep_26_seed68.json` | 17,134 | `d7644d69dcb51ed7854c9ae4328171bc42dbdad9e0f51ecfe8dd701105dca0f6` |
| `interest_free` | `ga` | `rep_27_seed69.json` | 17,118 | `5ff396871ee92ae75491191120baa1b96c5e5fffd75aa2cb071df550f73cfce8` |
| `interest_free` | `ga` | `rep_28_seed70.json` | 17,077 | `cbec062abb94c4e9893bab24e78d614e672bbc0da2795ef8706689ded91df1a4` |
| `interest_free` | `ga` | `rep_29_seed71.json` | 17,078 | `a8a6eba695e38bb13c2aca8c90d3d2e47225328163e63bf986eb1c5f97db76e4` |
| `interest_free` | `ga` | `rep_30_seed72.json` | 17,095 | `e7ab5c3f0995c7a7508af21786c03a92e74de83bc21a204157189204813fc735` |
| `interest_free` | `pso` | `rep_01_seed43.json` | 17,059 | `1fba199d41184eb41461a381561f527413718521f3dafeef4aa3f8e458f32776` |
| `interest_free` | `pso` | `rep_02_seed44.json` | 17,050 | `e7793de1b70053e592b5c0fd135ea96a4d126d57d0a770ef7f1a829b77957e03` |
| `interest_free` | `pso` | `rep_03_seed45.json` | 17,103 | `194c673eeb0e9c21b68f03a43585d1e033c244bc2a463237345db0387441f1e3` |
| `interest_free` | `pso` | `rep_04_seed46.json` | 17,147 | `53900ec68236d4ff4f424c6aa6c54514c6c1bc61f6aa856f159e3e6db97ca3d1` |
| `interest_free` | `pso` | `rep_05_seed47.json` | 17,126 | `6410bd3c49d27468ada9a90dc1214de873b458b207f3ecbd3661c21f33abef7e` |
| `interest_free` | `pso` | `rep_06_seed48.json` | 17,120 | `845e4ce57d2228725062a5e7f32694f0bba3c4a8bd2a7f9cee6a32509ea44d1a` |
| `interest_free` | `pso` | `rep_07_seed49.json` | 17,148 | `cb51d28f2a20d36f3c7deda808911a46e6db57287bc5d4699d9f14010a01100c` |
| `interest_free` | `pso` | `rep_08_seed50.json` | 17,131 | `f5f8bc1eba246932bbd2925a14b878026ca3896e2024951752bc679ce5cc9e4a` |
| `interest_free` | `pso` | `rep_09_seed51.json` | 17,063 | `01a4eced93ff0ca5e1b3b317a82c43d9cb57428a5ffec27edcd84496b7acc4ab` |
| `interest_free` | `pso` | `rep_10_seed52.json` | 17,098 | `27f11a521e1dffd10b3338ab58894e4f7217d93174d14fb9e48dff19d9218d1a` |
| `interest_free` | `pso` | `rep_11_seed53.json` | 17,065 | `64dc34dafaa9e5610d127d62fea03d49ec5feb17d4720ff9f18a88046166d72e` |
| `interest_free` | `pso` | `rep_12_seed54.json` | 17,100 | `ccd1d7f2cbe84571463b15cffc72bc34b923f4908dcd00bdcdd76d9a26c4cd4a` |
| `interest_free` | `pso` | `rep_13_seed55.json` | 17,131 | `e9e417700d2eb7d8af1473d92a4b9e2669a42a38219026922ec78311fe360b9f` |
| `interest_free` | `pso` | `rep_14_seed56.json` | 17,085 | `9a688e948dbd3f769ef53f285a524f5ceeca62c793a12aa63cf1bd360cd62f37` |
| `interest_free` | `pso` | `rep_15_seed57.json` | 17,127 | `9af7c507c0c89e1940ee75e03eafa387f459e657e5cc19ac8b05081af81761b7` |
| `interest_free` | `pso` | `rep_16_seed58.json` | 17,002 | `864bb22b8982f61d310a18c3fef66b9ca54023b75aaffe61a96a0491f6fbb774` |
| `interest_free` | `pso` | `rep_17_seed59.json` | 17,096 | `27764b51d732da793cad75cfff2bd9676743acb99d20d28c6b168b525ab2282f` |
| `interest_free` | `pso` | `rep_18_seed60.json` | 17,042 | `17aee59d5ff579957a9382bb0e89091cd71a208b9ef51ff2c63fba05a0764c60` |
| `interest_free` | `pso` | `rep_19_seed61.json` | 17,060 | `cb4c1f875e4da5d8e14989d2a16ea7782459fb10efb51937b029192776734dee` |
| `interest_free` | `pso` | `rep_20_seed62.json` | 17,100 | `d6be5e6c5e4186f038dfc44c6815ee480f630b4e5215fdbfa2b05be944385df8` |
| `interest_free` | `pso` | `rep_21_seed63.json` | 17,080 | `1e7a3d03d031b18d55583f344e34295a5b1ce2699f8961af7f781337df691317` |
| `interest_free` | `pso` | `rep_22_seed64.json` | 17,068 | `b2bd247e19222ffe6793453043f85d0751b184d70952f9406c04a50bcb63fc7f` |
| `interest_free` | `pso` | `rep_23_seed65.json` | 17,114 | `6f4eb741acf7d4fe44fbdf649a9b7960bbec60caaabcb25f6f57a98e16fff170` |
| `interest_free` | `pso` | `rep_24_seed66.json` | 17,082 | `b58dee6a00cd27d4ec10684d5b69f200247e47d6a235011de19c590069b46c44` |
| `interest_free` | `pso` | `rep_25_seed67.json` | 17,012 | `1e76ed38d4f22875e8b61879021e49ae67f269dac19bcbc401fbccc717425f2b` |
| `interest_free` | `pso` | `rep_26_seed68.json` | 17,150 | `814849e1366beff969f73b5e7bcfe67b47120f470609f9a71140268d9e5eda78` |
| `interest_free` | `pso` | `rep_27_seed69.json` | 17,116 | `a039bb35bcf6d8cc45454a0401209f4bc593246a1abf73a2431f190550cf29a4` |
| `interest_free` | `pso` | `rep_28_seed70.json` | 17,048 | `41ed6f9334b2c0221c2a7cebaac60383e4a779f78ae37f40a64c3168ec37e48f` |
| `interest_free` | `pso` | `rep_29_seed71.json` | 17,116 | `7cfb2a5a478e5d64fe5616ae14e58bd818852b3cd41642f552e217170e2fe53c` |
| `interest_free` | `pso` | `rep_30_seed72.json` | 17,118 | `ffc86bdc502283346f209331b2b062592cebd9c33515b6f0de1d4911a0a9f537` |
| `interest_djppr` | `kma` | `rep_01_seed43.json` | 17,134 | `152f8f06a421807aa2e9f9dcb18839d92156c50f94298d2dff1ae365611aae9e` |
| `interest_djppr` | `kma` | `rep_02_seed44.json` | 17,126 | `5471ddec106772e2cc70f513571e050613f198615f694439afb98e460f776c9d` |
| `interest_djppr` | `kma` | `rep_03_seed45.json` | 17,043 | `d5e28b5c542081ab78c4ac184654f9c0933c685bd37dc5b3b5ffea68aee855e1` |
| `interest_djppr` | `kma` | `rep_04_seed46.json` | 17,110 | `7568caee1de0059863e6fdcc845b16b7fafc48143d4cb915d3dfd6f352f05985` |
| `interest_djppr` | `kma` | `rep_05_seed47.json` | 17,078 | `9dbf550c6eb1d6cc959b3f53a3453781d8e3db599ff70af396b2d42130ce05b2` |
| `interest_djppr` | `kma` | `rep_06_seed48.json` | 17,029 | `5f152411eb67c3046df02388a6fcd58f426504034b7e43801893019dcc91674e` |
| `interest_djppr` | `kma` | `rep_07_seed49.json` | 17,030 | `7a077c592753c53c081095208d6bb067bed7ac2425fa88c6b8bb44363cc3e47b` |
| `interest_djppr` | `kma` | `rep_08_seed50.json` | 16,971 | `d8b77fd9984fa667f0b92ea8e01f4f061461c276f413d28a8a336712f949e2f8` |
| `interest_djppr` | `kma` | `rep_09_seed51.json` | 17,083 | `c10492c5052a6d694399ea43befb248ed0697105582696128cc795743ce9ecaa` |
| `interest_djppr` | `kma` | `rep_10_seed52.json` | 17,029 | `e2915e95cb4fc6b97142970058a11d00230bb52769dc33a4271c8c9865b1be72` |
| `interest_djppr` | `kma` | `rep_11_seed53.json` | 17,206 | `f8bde1aa15b97770380008f475c3303def768689060208b3ed1829ae7ae12492` |
| `interest_djppr` | `kma` | `rep_12_seed54.json` | 17,033 | `1854190541e2fce108873154b9e298dd9cb3e754f0134b45f214ca9f4ab32906` |
| `interest_djppr` | `kma` | `rep_13_seed55.json` | 17,191 | `a8fe951825eaf1d12353aa74989436c911af87de16284bc2eed116b9cfc16b3c` |
| `interest_djppr` | `kma` | `rep_14_seed56.json` | 17,115 | `625f670e1cdc80c35550e134182fa722dc8c4db5e90a8b28083020bbdff26f12` |
| `interest_djppr` | `kma` | `rep_15_seed57.json` | 17,110 | `066568dad8e280a2c997bc1adc9b58391948faf626d6cd2a3ba1773f7edfd113` |
| `interest_djppr` | `kma` | `rep_16_seed58.json` | 17,094 | `3ea4088df3e8e9584992d74e1ee65c5b08eee1d15bcefa0aa1c703520b55c51c` |
| `interest_djppr` | `kma` | `rep_17_seed59.json` | 16,979 | `371099111f8bba5b6bee0203191ec6cbd550dc573a3a86f88d34be6fb2408b9b` |
| `interest_djppr` | `kma` | `rep_18_seed60.json` | 17,031 | `eeb275481174c9fbb516bdab729c81d2f0a696627b4b57c8d4924983fb4c3e86` |
| `interest_djppr` | `kma` | `rep_19_seed61.json` | 17,083 | `10c28699f1e7360bcb8267e4590a6c4cf696d72400426c0ef6d62855d985b143` |
| `interest_djppr` | `kma` | `rep_20_seed62.json` | 17,090 | `766c174603c084a1425865f6e46f9cb0b29d95b023bcaa399a91dc1720710e69` |
| `interest_djppr` | `kma` | `rep_21_seed63.json` | 17,099 | `c4e4369fa593d0273993d7c252b07b5a5df106b2fb1d837dda178db3f18c5a71` |
| `interest_djppr` | `kma` | `rep_22_seed64.json` | 17,033 | `de0d2d986a1f96dd5d0a4739413086b407aca3e47bc57b04c6c3760b6110f60a` |
| `interest_djppr` | `kma` | `rep_23_seed65.json` | 17,092 | `5de30e91cdea6475d880938627741b90acb89bceae1ff4c2fabc5882ad6e13c2` |
| `interest_djppr` | `kma` | `rep_24_seed66.json` | 17,215 | `9be9143f1bf8460e6806d3d3abcc23642f9cbc662ec6bce433a5c4e86347b2a2` |
| `interest_djppr` | `kma` | `rep_25_seed67.json` | 17,148 | `08c2302e11befa632731a579fa0264d6db4bdfb1ff9221aff58f6000c30e84ac` |
| `interest_djppr` | `kma` | `rep_26_seed68.json` | 17,025 | `22893441f8bd5005b0cc28299e709c8af30d6f5491f46728321e3bfe3599fa90` |
| `interest_djppr` | `kma` | `rep_27_seed69.json` | 17,060 | `34c2f17fc2aca68301ce7fd6a733965daf93be8c5b6d2558a127924d66ed8f39` |
| `interest_djppr` | `kma` | `rep_28_seed70.json` | 17,210 | `1a89e28f1c3ac4639290ad2df0ae2894716c6296315fa4c2d0675048cf28fe9d` |
| `interest_djppr` | `kma` | `rep_29_seed71.json` | 17,029 | `5f19162706949a19e7aa1584e3088732e5dec19f6f6899d9e1d5fad8a26451d6` |
| `interest_djppr` | `kma` | `rep_30_seed72.json` | 17,163 | `02f393c986aa46c414a0ef048bab620067060a0d85934c8c42a9d003a30311d6` |
| `interest_djppr` | `ga` | `rep_01_seed43.json` | 17,069 | `f4965412d519c91fc5c08824ad84e481e3c3fc2dcf3760934e50d39bf064ee5f` |
| `interest_djppr` | `ga` | `rep_02_seed44.json` | 17,084 | `53f3396659273fa4ff1a3bc59842ce0faa57734430c4815d132715e51e23b3a9` |
| `interest_djppr` | `ga` | `rep_03_seed45.json` | 17,084 | `43ef2ef77d8928e1098ed701aba2230f77e1492b169a9f1527620a1a4e46197c` |
| `interest_djppr` | `ga` | `rep_04_seed46.json` | 17,075 | `8d6badc3f5f6271c3bcd274d261e48e569db6d1a6eceee0f3938b65cbdc2fcd6` |
| `interest_djppr` | `ga` | `rep_05_seed47.json` | 17,064 | `69e16a8eddca16b91d1b886ad1046ac60ec3d7f0fc866f74a434b27aa9e3234a` |
| `interest_djppr` | `ga` | `rep_06_seed48.json` | 17,037 | `06609d7a3fca05d522756d20a057ea731d70ee2f9b23c8950d4fa246bc18fab0` |
| `interest_djppr` | `ga` | `rep_07_seed49.json` | 17,089 | `6b95bd3401aaa2a9a889ff1598105a98dfc7acec9c78efc2ada8a033585e2e9d` |
| `interest_djppr` | `ga` | `rep_08_seed50.json` | 17,054 | `5c185db9496719acc7c19eebe8c71a12c90665c0827c6920b5bd04838f84c6a7` |
| `interest_djppr` | `ga` | `rep_09_seed51.json` | 17,065 | `95a698a2d09435c74227ce821802f00e6065a796f5058e6d780d0f2c371b26bf` |
| `interest_djppr` | `ga` | `rep_10_seed52.json` | 17,056 | `0758662e635e43d1c28e1ae9051df82d832899eab3532430879f8cae5d0f19e8` |
| `interest_djppr` | `ga` | `rep_11_seed53.json` | 17,091 | `9a3a3b21c904863551f9a6ec8c65535d3e677e481a223bbaeaf609924ef508fb` |
| `interest_djppr` | `ga` | `rep_12_seed54.json` | 17,059 | `78be29c22a007a4ad7e8950b4feba63bf17a1fe3e1587040bddc7c0c23137ca5` |
| `interest_djppr` | `ga` | `rep_13_seed55.json` | 17,068 | `7be6700f19e6739fd2c0d7fe5aa401775e5d476f4fe99fb5d7c83187d70da34f` |
| `interest_djppr` | `ga` | `rep_14_seed56.json` | 17,061 | `6ce6ffa1014a247e0c6c8509ebec4bab81f79f5904dd312040b306d281046c63` |
| `interest_djppr` | `ga` | `rep_15_seed57.json` | 17,089 | `2af94d4f1ecfaa63efbd099967a54408bda23a68d6a55e0e19229f1c9e54e485` |
| `interest_djppr` | `ga` | `rep_16_seed58.json` | 17,053 | `e2f64b6f48254e66763546e15381bb0da673f4da7c69d9dce791c7db1997abea` |
| `interest_djppr` | `ga` | `rep_17_seed59.json` | 17,060 | `9a581e1e00223fcbdd4c18f818c7f34352335baf575278c1eddf20f0984dd518` |
| `interest_djppr` | `ga` | `rep_18_seed60.json` | 17,034 | `fa78a01b1ed147527c2cf8b3c2ebd10b4bf76053ac75cb9b3a6cebe280403881` |
| `interest_djppr` | `ga` | `rep_19_seed61.json` | 17,048 | `ea343f47ffc71a9836dbc085226d3fb34900201d940cabade104340746409376` |
| `interest_djppr` | `ga` | `rep_20_seed62.json` | 17,040 | `0910518eed4b5b2c8b53917d0a79d02c363ae3851ddfbffe58ab9aae908e50e8` |
| `interest_djppr` | `ga` | `rep_21_seed63.json` | 17,021 | `6f1c72e03042a00fef0c64313ed9ee60eaf07af2155a1008237a5c50a1cd0c49` |
| `interest_djppr` | `ga` | `rep_22_seed64.json` | 17,050 | `36b471393f92358a890883173b8ff031429fdda4acd75a21ffc7f2212b6bf937` |
| `interest_djppr` | `ga` | `rep_23_seed65.json` | 17,108 | `3b08a263bd3392ab2d669cf5e60509a41d4578878906db3d25618b7ac9c565d9` |
| `interest_djppr` | `ga` | `rep_24_seed66.json` | 17,015 | `decc52fb340be217a3e199fcb46d7f35b48de370b004e0e6d1884f328c702d82` |
| `interest_djppr` | `ga` | `rep_25_seed67.json` | 17,026 | `dd9623bc0f73ad085d192e804ccbb9ee4cccf7421314aa733ed2033b6a8ea56c` |
| `interest_djppr` | `ga` | `rep_26_seed68.json` | 17,040 | `efe37be8c377fb36b95f5f50ae5586918d50085088e68910e25f9b4da1e9b3b1` |
| `interest_djppr` | `ga` | `rep_27_seed69.json` | 17,069 | `74f53d09c22a59b8f22038a18cccff8530fcd719e65bf8b58c1a8b6d0eab05e1` |
| `interest_djppr` | `ga` | `rep_28_seed70.json` | 17,035 | `6ad574230bfba5d9542d592dc8eb8b21671cf043250beaf82bea8bac162d9da6` |
| `interest_djppr` | `ga` | `rep_29_seed71.json` | 17,037 | `f87510332e9b4f3819f1e5fd509322b3450a972a43327dab6ed966a47ee0dd57` |
| `interest_djppr` | `ga` | `rep_30_seed72.json` | 17,049 | `3a9b870d92205d1acb40d4a6a131264f3dcf72927aa6f511dd8d6c074404d8d2` |
| `interest_djppr` | `pso` | `rep_01_seed43.json` | 17,029 | `771a888be043289e392b63d17219f65d358090ce03eff6308f5031a02c5a5a4d` |
| `interest_djppr` | `pso` | `rep_02_seed44.json` | 17,038 | `3b91b1b76b3f168281efd83846875e07e39c1f46c8666ce72195c6a5935539b4` |
| `interest_djppr` | `pso` | `rep_03_seed45.json` | 16,978 | `58130c7e3847a66ebf83e29c7ebfdff7d0170e17fd0531ca390abdba16b158a8` |
| `interest_djppr` | `pso` | `rep_04_seed46.json` | 16,981 | `ebfbe8364bf06bbb0dcaa4236eaf8654e2a7e233014a2cf8639f053003c0a4ed` |
| `interest_djppr` | `pso` | `rep_05_seed47.json` | 17,036 | `14b7fc7d5bea816eb53ac6d7cbe5640c4ccafaad0ad68d77b2ab3004e3ce9523` |
| `interest_djppr` | `pso` | `rep_06_seed48.json` | 17,038 | `15daa8f2ca348e195f25a9654604ea4eb36e9fce6fa29209bdb7f51626170633` |
| `interest_djppr` | `pso` | `rep_07_seed49.json` | 17,032 | `df7414fe3e40a7989df96d12a3629d28d9e261ad6fdc096313e1582aad3574a6` |
| `interest_djppr` | `pso` | `rep_08_seed50.json` | 17,027 | `8d9fbe3b157a6b30127b177e5f24acc95602e366910fdd06a794bd6db6de1da8` |
| `interest_djppr` | `pso` | `rep_09_seed51.json` | 17,036 | `120f3104f478a96d08f26e7526366420a9e4bb11ae3fd9b80ef105764a681121` |
| `interest_djppr` | `pso` | `rep_10_seed52.json` | 17,038 | `314a7e07fd5a5ac01b8bc4552fc408c4a33b24f6cf3980132e211d6c5ade55f6` |
| `interest_djppr` | `pso` | `rep_11_seed53.json` | 17,028 | `323c1ca88955d235f5e1918005fa699f8b1f84e8a517d8867ddc73b4e8c41abc` |
| `interest_djppr` | `pso` | `rep_12_seed54.json` | 16,949 | `a18ff4ab304e05718bcd86f86f45b19d444bbdab35cfcfa730f43510e1e132e1` |
| `interest_djppr` | `pso` | `rep_13_seed55.json` | 16,944 | `517e10fe9a5435478dbd7732a39af352ab15e63d49cb5b97621ecae10c0aa9c7` |
| `interest_djppr` | `pso` | `rep_14_seed56.json` | 17,030 | `cc74071835620cd3134986b8a60e98cf588ddd790cd608ef7390447290747b86` |
| `interest_djppr` | `pso` | `rep_15_seed57.json` | 17,044 | `f9b10549081ad204a94c77492aaf999fba6f0dadadb53587dfbf588623999e23` |
| `interest_djppr` | `pso` | `rep_16_seed58.json` | 17,041 | `f6db5bd710ac162ad75096ab0e23ecc833ac27ca0bc08a009781f7cb98b95492` |
| `interest_djppr` | `pso` | `rep_17_seed59.json` | 16,987 | `07e74c6f541ba719eb4cea320f01181bba4e0339e778ae9432a512e7d4df6097` |
| `interest_djppr` | `pso` | `rep_18_seed60.json` | 17,038 | `d79ae5f4bf6997fff7c6f047507f5295d8c0ec13915724191e2931807f0c7566` |
| `interest_djppr` | `pso` | `rep_19_seed61.json` | 17,030 | `911349ed91d0431fddba7a381ddb8adda3fedaa79a4f287734825dfed60ce5be` |
| `interest_djppr` | `pso` | `rep_20_seed62.json` | 17,031 | `a30a4917c76222f35da78e59b97de27c570f32f43f6122fd6aeba25daa4b4cbc` |
| `interest_djppr` | `pso` | `rep_21_seed63.json` | 17,041 | `1dccc20f15577edfda7292fbea32bcad302e168d98b3079b6d176696f3d30a0a` |
| `interest_djppr` | `pso` | `rep_22_seed64.json` | 17,042 | `4fc3dfb4621e89fa3a6181016271468eee3bd9297f34433b7fda043e292f23bb` |
| `interest_djppr` | `pso` | `rep_23_seed65.json` | 17,040 | `dd36a4c2edfe39b6fc310d832c086f7a48b27fca4a6bf1b71249a4682524ae67` |
| `interest_djppr` | `pso` | `rep_24_seed66.json` | 16,987 | `db02436127b52d9c72a606a30f529f8157252bdac7dc752ae850790fb08c7cbb` |
| `interest_djppr` | `pso` | `rep_25_seed67.json` | 17,038 | `812f4fb7d87aee46e728a4bbf3d90f1f4995dc37935853ad019d5b7d0fe04ac2` |
| `interest_djppr` | `pso` | `rep_26_seed68.json` | 17,008 | `c5dc81a69ee42c30d89a236cd3e24cb9b13d489a1b2b3aef694df07b9a5d1796` |
| `interest_djppr` | `pso` | `rep_27_seed69.json` | 17,037 | `89fba4b9b643a855b61c4a4d03f9a58b04c29bc8fabde0170b51e1904d676740` |
| `interest_djppr` | `pso` | `rep_28_seed70.json` | 17,087 | `d763b413c25fd6a536c54199f89b6e145b11e36ba6060f9e395b7b7a2e35faf5` |
| `interest_djppr` | `pso` | `rep_29_seed71.json` | 17,037 | `badb7200cfd92eb94b470a2c63846fde2427b9b587151257af4a561fbb7f9385` |
| `interest_djppr` | `pso` | `rep_30_seed72.json` | 17,043 | `41a9fa3b7646343fac59844da30e6445b4cb1ebc7427a430d62e6516cf3204ca` |

</details>

---

## 5. Verifikasi Keaslian Berkas

Untuk memverifikasi keaslian seluruh berkas hasil di repositori ini, jalankan:

```powershell
# Windows PowerShell
Get-FileHash results/tables/runs_summary.csv -Algorithm SHA256
Get-FileHash results/tables/tab_results_summary.tex -Algorithm SHA256
```

```bash
# Linux / macOS
sha256sum results/tables/runs_summary.csv
sha256sum results/tables/tab_results_summary.tex
```

Nilai yang dihasilkan wajib sama persis dengan tabel di atas.