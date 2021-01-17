# size_dist.py
Calculate size distribution of reads from fastq and bam files.

## Install
`size_dist.py` is a python3 executable script that relies on the
[pysam](https://pysam.readthedocs.io/en/latest/index.html) library. To install
use conda to create an environment that contains `pysam`, then add the
`size_dist.py` script to that environment's bin/.

First, install conda using miniconda. [The instructions at the Bioconda page](https://bioconda.github.io/user/install.html)
are great to get started with installing conda / miniconda.

Next, create and activate a conda environment to hold `pysam` and `size_dist.py`.
The `conda config` commands ensure the bioconda and r channels are available;
required for pysam installation.
```
conda create --name size_dist
conda activate size_dist
conda config --add channels r
conda config --add channels bioconda
conda install pysam
```

Now, [download the latest release as .zip from github.](https://github.com/MikeAxtell/size_dist/releases) Unzip it, then copy the script into your environment's /bin/
folder:
```
unzip size_dist-main.zip
cp size_dist-main/size_dist.py /path/to/miniconda3/envs/size_dist/bin/
```
In the above, be sure to replace `/path/to` with the correct path to your
miniconda3 installation. (Call `conda env list` to find this.)

## Usage
```
usage: size_dist.py [-h] [-s] [-d] [-c] [-u] [-v] files [files ...]

positional arguments:
  files                 One or more .bam or .fastq files

optional arguments:
  -h, --help            show this help message and exit
  -s, --includeSupplementary
                        Include supplementary alignments (bam)
  -d, --includeDuplicate
                        Include duplicate alignments (bam)
  -c, --includeSecondary
                        Include secondary alignments (bam)
  -u, --excludeUnmapped
                        Exclude unmapped reads (bam)
  -v, --version         show program's version number and exit

```
Files must end in either `.bam` or `.fastq`. Compressed fastq files are not
accepted.

For bam files, by default, supplementary, secondary, and duplicate reads are
excluded, while unmapped reads are included. Optional switches are available to
change the default behaviors for these alignment types. Each line in a bam file
(unless excluded) is treated as a separate read.

## Output
Output goes to STDOUT and is a tab-separated table of data. Example:
```
File	Size	Frequency	Fraction
GSM854154.bam	15	1759	0.00027750760621686455
GSM854154.bam	16	4626	0.0007298181843997814
GSM854154.bam	17	13391	0.0021126232830301498
GSM854154.bam	18	35733	0.005637395845905185
GSM854154.bam	19	85765	0.01353066506378021
GSM854154.bam	20	163466	0.02578911788393745
GSM854154.bam	21	841528	0.13276317273704694
GSM854154.bam	22	793279	0.12515119747135195
GSM854154.bam	23	916409	0.14457672990653248
GSM854154.bam	24	3354232	0.5291784496964218
GSM854154.bam	25	73939	0.011664943090431352
GSM854154.bam	26	18068	0.0028504874526016537
GSM854154.bam	27	12488	0.00197016201616612
GSM854154.bam	28	10181	0.0016061995104570197
GSM854154.bam	29	8467	0.001335791302921087
GSM854154.bam	30	5234	0.0008257389487999256
SRR538253_3Q.fastq	15	296557	0.021785068467630894
SRR538253_3Q.fastq	16	1217523	0.08943920364690554
SRR538253_3Q.fastq	17	200180	0.014705216892032061
SRR538253_3Q.fastq	18	271500	0.019944381987145092
SRR538253_3Q.fastq	19	675642	0.049632641379589996
SRR538253_3Q.fastq	20	465788	0.03421677273306939
SRR538253_3Q.fastq	21	1155131	0.08485588916829796
SRR538253_3Q.fastq	22	1542157	0.11328680770589214
SRR538253_3Q.fastq	23	1593121	0.11703062164177745
SRR538253_3Q.fastq	24	4712381	0.3461713691821907
SRR538253_3Q.fastq	25	226844	0.016663953545090024
SRR538253_3Q.fastq	26	234109	0.01719764023067606
SRR538253_3Q.fastq	27	172600	0.012679190906008261
SRR538253_3Q.fastq	28	103973	0.007637853511415973
SRR538253_3Q.fastq	29	115397	0.008477060214256288
SRR538253_3Q.fastq	30	193766	0.014234044641330225
SRR538253_3Q.fastq	31	357317	0.026248496274404138
SRR538253_3Q.fastq	32	44771	0.0032888763386610424
SRR538253_3Q.fastq	33	34099	0.002504911533626742
```
