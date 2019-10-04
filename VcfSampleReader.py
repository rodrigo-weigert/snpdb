from SampleReader import SampleReader
import tempfile
import os

class VcfSampleReader(SampleReader):

    def __iter__(self):
        with open(self._PED_FILE) as f:
            header = None
            for line in f:
                if line[0:2] != "##":
                    header = line.split()
                    break
            sample_strs = [header[i] + " " for i in range(9, len(header))]
            for line in f:
                tokens = line.split()
                if len(tokens) != len(header):
                    raise Exception("Missing column value.")
                for i in range(9, len(tokens)):
                    sample_strs[i-9] += tokens[i] + " "
        for i, sample_str in enumerate(sample_strs):
            snps = sample_str.split()
     
            gen = {"g": snps[1:]}
            sample = {self.SAMPLE_ID: snps[0],
                      self.SAMPLE_GENOTYPE: gen}
            yield sample


    def __len__(self):
        try:
            return self.__len
        except:
            pass
        with open(self._PED_FILE) as f:
            for line in f:
                if line[0:2] != "##":
                    self.__len = len(line.split())-9
                    break
        return self.__len
                

