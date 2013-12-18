This is the statistic computation scripts.
==

* fastq2reads: get reads from fastq format file

* count.py: computing ACGT count

* gc.py: computing gc percentage

* orf.py: computing the number of possible proteins in a given dna segment. import geneFormat, revc

  *  geneFormat: dna format, dna --> rna translation and rna-->protein transcription 

  *  revc: get the reverse complement strand of a given dna

* hamm.py:computing hamilton distance

* edta.py:computing edit distance

* assembly.py: genome sequence assembly, which import dc, overlap, layout

  *  dc.py: get suffix array from reads

  *  overlap: get overlap links from suffix array

  *  layout: remove replicated links from overlap


