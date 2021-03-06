//
//  main.m
//  cbase
//
//  Created by Quanlong He on 9/2/13.
//  Copyright (c) 2013 Quanlong He. All rights reserved.
//

#import <UIKit/UIKit.h>

#import "CKAppDelegate.h"

#include "chromium/base/at_exit.h"
#include "chromium/base/command_line.h"
#include "chromium/base/logging.h"

int main(int argc, char *argv[])
{
  base::AtExitManager exit_manager;
  CommandLine::Init(argc, argv);
  VLOG(0) << "This is log print by libchromium";
  
  @autoreleasepool {
      return UIApplicationMain(argc, argv, nil, NSStringFromClass([CKAppDelegate class]));
  }
}
