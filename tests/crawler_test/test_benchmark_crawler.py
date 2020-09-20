import unittest
import os
import sys
import pandas as pd
import numpy as np
from urllib.error import URLError, HTTPError

sys.path.insert(0, '../../crawler')
from benchmark_crawler import scrape

class test_crawler(unittest.TestCase):
    # Unit test for the crawler function (scrape).
    @classmethod
    def setUpClass(cls):
        print("\nStarting up testing...")

        # Initialise benchmark websites to test online data scraping.
        cls.web_cpu = 'https://www.cpubenchmark.net/cpu_list.php'
        cls.web_gpu = 'https://www.videocardbenchmark.net/gpu_list.php'

        # Initialise .html files to test offline data scraping.
        cls.file_cpu = 'Webpage_CPUBenchmark.html'
        cls.file_gpu = 'Webpage_GPUBenchmark.html'

        # Initialise correct result .csv files (checked datasets) to compare with scrape function result.
        cls.res_cpu = 'CPUResult.csv'
        cls.res_gpu = 'GPUResult.csv'

        # Initialise output result .csv files.
        cls.out_web_cpu = 'WEB_CPUResult.csv'
        cls.out_web_gpu = 'WEB_GPUResult.csv'
        cls.out_cpu = 'FILE_CPUResult.csv'
        cls.out_gpu = 'FILE_GPUResult.csv'

        # Initialise output test .csv files.
        cls.out_test_file = 'TEST_OUTPUT.csv'
        cls.out_test_web = 'TEST_OUTPUT2.csv'

        # Initialise data columns for dataframe data sorting.
        cls.col_cpu = 'CPU Name'
        cls.col_gpu = 'Videocard Name'

        print("Successfully initialised testing variables!\n")

    @classmethod
    def tearDownClass(cls):
        print("\nFinishing up testing...")
        file_list = [cls.out_cpu, cls.out_gpu, cls.out_test_file, cls.out_web_cpu, cls.out_web_gpu]
        [os.remove(file) for file in file_list]
        print("Successfully deleted test files!")

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            scrape('string', 'output.csv', 'web')
        with self.assertRaises(FileNotFoundError):
            scrape('string', 'output.csv', 'file')
        with self.assertRaises(OSError):
            scrape('https://www.cpubenchmark.net/cpu_list.php', 'output.csv', 'file')
        with self.assertRaises(URLError):
            scrape('https://ww.cpubenchmark.net/cpu_list.php', 'output.csv', 'web')
        with self.assertRaises(HTTPError):
            scrape('https://www.cpubenchmark.net/cpu_list.phpa', 'output.csv', 'web')

    def test_results_from_web(self):
        print('\nTesting web results. If any differences are found, this test may fail.\nDo update the webpage and result files if this test fails.')

        scrape(self.web_cpu, self.out_web_cpu, 'web')
        col1 = pd.read_csv(self.res_cpu).loc[:, self.col_cpu].to_list()
        col2 = pd.read_csv(self.out_web_cpu).loc[:, self.col_cpu].to_list()
        print('CPU COL Differences:', np.setxor1d(col1, col2))
        self.assertEqual(all(cpu in col2 for cpu in col1), True)

        scrape(self.web_gpu, self.out_web_gpu, 'web')
        col1 = pd.read_csv(self.res_gpu).loc[:, self.col_gpu].to_list()
        col2 = pd.read_csv(self.out_web_gpu).loc[:, self.col_gpu].to_list()
        print('GPU COL Differences:', np.setxor1d(col1, col2))
        self.assertEqual(all(gpu in col2 for gpu in col1), True)

    def test_results_from_file(self):
        scrape(self.file_cpu, self.out_cpu, 'file')
        df1 = pd.read_csv(self.res_cpu).sort_values(self.col_cpu)
        df2 = pd.read_csv(self.out_cpu).sort_values(self.col_cpu)
        equivalence = df1.equals(df2)
        self.assertEqual(equivalence, True)

        scrape(self.file_gpu, self.out_gpu, 'file')
        df1 = pd.read_csv(self.res_gpu).sort_values(self.col_gpu)
        df2 = pd.read_csv(self.out_gpu).sort_values(self.col_gpu)
        equivalence = df1.equals(df2)
        self.assertEqual(equivalence, True)

    def test_output_presence(self):
        path = scrape(self.file_cpu, self.out_test_file, 'file')
        self.assertEqual(os.path.exists(path), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)