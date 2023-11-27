from main import main
import unittest
import os
import sys
from io import StringIO


class testCase(unittest.TestCase):

    def _getStdout(self, callback, *args) -> str:
        """Sniffs Stdout and returns it as a string to be tested
        Args:
        callback(Any): A function to call
        args(Any[]): Arguments for the callback

        Returns:
        str: Contents of Stdout
        """
        sys.stdout = buffer = StringIO()
        callback(*args)
        sys.stdout = sys.__stdout__
        return buffer.getvalue()


    def _test_func(self, testCase: int) -> None:
        """Tests the following function processing inputs with main.main and comparing outputs
        
        Args:
        testCase(int): The case file to check

        """
        # test code here
        istream = open(os.path.join("testCases", str(testCase) + ".in"), 'r') # Input file
        ostream = open(os.path.join("testCases", str(testCase) + ".out"), 'r') # Output file
        cnt = 1

        # 1 Input, 1 Output
        for input_data in istream.readlines():
            output_data = ostream.readline()
            # output = self._getStdout(main, input_data.rstrip())
            output = main(input_data.rstrip)
            print(f"Test Case {cnt}: {output}")
            try:
                self.assertEqual(output.rstrip(), output_data.rstrip()) # Test the case
            except Exception as e:
                istream.close()
                ostream.close()
                raise e
            cnt += 1



        



    def testCase1(self): self._test_func(1)

    @unittest.skipUnless("".join(list(filter(lambda x: x=="2.in", os.listdir("testCases")))), "Could not find a second test case")             
    def testCase2(self): self._test_func(2)

    @unittest.skipUnless("".join(list(filter(lambda x: x=="3.in", os.listdir("testCases")))), "Could not find a third test case")             
    def testCase3(self): self._test_func(3)




if __name__ == "__main__":
    unittest.main()