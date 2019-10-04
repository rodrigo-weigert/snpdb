#!/usr/bin/env python3
import argparse
import snpdb
import time

from Zero125SampleReader import Zero125SampleReader
from PlinkSampleReader import PlinkSampleReader
from FinalReportSampleReader import FinalReportSampleReader
from VcfSampleReader import VcfSampleReader

Z125 = 0
PLINK = 1
ILMFR = 2
VCF = 3

READERS = [Zero125SampleReader, PlinkSampleReader,
          FinalReportSampleReader, VcfSampleReader]

def import_samples(filename, fileformat, mapname, **kwargs):
   reader = READERS[fileformat](filename)
   snpdb.import_samples(reader, mapname, **kwargs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("format", help="map file format",
                        choices=["vcf", "fr", "z125", "pl"])
    parser.add_argument("samplefile", help="samples file path")
    parser.add_argument("mapname", help="id of the map to be used"+ 
                                        "(must exist in the database)")
    parser.add_argument("-q", "--quiet", help="omit all output",
                        action="store_true")
    args = parser.parse_args()

    if args.format == "vcf":
        fmt = VCF
    elif args.format == "fr":
        fmt = ILMFR
    elif args.format == "z125":
        fmt = Z125
    else:
        fmt = PLINK
    
    report = not args.quiet

    start = time.time()

    import_samples(args.samplefile, fmt, args.mapname,
                   report=report)
    
    if report:
        print(f"Done in {time.time() - start:.3f} s.")