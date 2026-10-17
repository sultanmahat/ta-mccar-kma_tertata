# Proposal Tugas Akhir — Sultan Bakri Baihaqi Mahat (MCCaR + KMA)

Format mengikuti template PROPOSAL (folder proposal/, proposal-main.tex, \pagestyle{proposal}).
Berisi BAB 1-3 + Jadwal Kegiatan. Topik: Optimasi Portofolio Utang Negara Multivaluta
dengan model MCCaR menggunakan Komodo Mlipir Algorithm.

## Isi yang sudah dikerjakan
- proposal/contents/000_metadata.tex   -> judul, Nama Sultan Bakri Baihaqi Mahat, NRP 5002221016,
  Kaprodi Dr. Tahiyatul Asfihani, Pembimbing Prof. DR. Mohammad Isa Irawan, MT (NIP 19631225 198903 1 001)
- proposal/contents/001_intro.tex      -> BAB 1 Pendahuluan
- proposal/contents/002_literature.tex -> BAB 2 Tinjauan Pustaka (MVO, GBM, CCaR, MCCaR, KMA, dll.)
- proposal/contents/003_method.tex     -> BAB 3 Metode Penelitian
- proposal/contents/004_schedule.tex   -> Jadwal Kegiatan (Gantt, disesuaikan alur MCCaR+KMA)
- proposal/contents/100_symbols.tex    -> Daftar Simbol (MCCaR/KMA)
- proposal/contents/XXX_abstrak.tex    -> Abstrak (ID)
- proposal/contents/XXX_abstract.tex   -> Abstract (EN)
- proposal/assets/pustaka.bib          -> 18 entri MCCaR/KMA ditambahkan di akhir file
- proposal/compile-here/proposal-main.tex -> \method=Komodo Mlipir Algorithm; ditambah \usepackage{longtable} & {enumitem}

## Cara compile (dari ROOT folder ini, tempat TA-ITS.cls berada)
    pdflatex proposal/compile-here/proposal-main.tex
    bibtex   proposal-main
    pdflatex proposal/compile-here/proposal-main.tex
    pdflatex proposal/compile-here/proposal-main.tex
Sudah diuji: menghasilkan PDF 34 halaman, tanpa error LaTeX, tanpa sitasi/ref undefined.

## TODO Anda
- Tambah diagram alir di BAB 3 (placeholder fig:flowchart-mccar sudah ada, taruh PNG di proposal/assets/images/)
- Lengkapi tanggal disetujui di 000_metadata.tex bila sudah ACC
- Cek kemiripan (Turnitin) BAB 2 terhadap Kajian DJPPR & TA Fauzan

## Update: Gambar (diagram)
- proposal/contents/fig_flowchart.tex -> Diagram Alir Penelitian (TikZ), di-\input dari 003_method.tex
- proposal/contents/fig_skema.tex     -> Skema dan Posisi Penelitian (TikZ), di-\input dari 001_intro.tex
Keduanya vektor TikZ (bukan PNG), jadi tajam & otomatis ikut font dokumen.
Library TikZ (shapes.geometric, arrows.meta, positioning, calc, fit, backgrounds)
dideklarasikan di dalam masing-masing file figur.
