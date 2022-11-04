#include <stdio.h>
#include <iostream>
#include <opencv2/calib3d.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

using namespace cv;
using namespace std;
const char* previewHelp =
    "Preview functions:\n"
        "  <ESC>, 'q' - quit the program\n"
        "  'u' - toggle undistortion on/off\n"
        "  'c' - toggle ArUco marker coordinates/IDs\n";#include <iostream>


int main(int argc, char **argv) {

  (void)argc;
  (void)argv;

  std::vector<cv::String> fileNames;
  cv::glob("../calibration/Image*.png", fileNames, false);
  cv::Size patternSize(25 - 1, 18 - 1);
  std::vector<std::vector<cv::Point2f>> q(fileNames.size());
