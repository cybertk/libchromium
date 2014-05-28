//
//  ViewController.m
//  cbase
//
//  Created by Quanlong He on 9/2/13.
//  Copyright (c) 2013 Quanlong He. All rights reserved.
//

#import "ViewController.h"

#include "chromium/base/bind.h"
#include "chromium/base/memory/scoped_ptr.h"
#include "chromium/base/message_loop.h"

void DoSomething() {
  DVLOG(0) << "Print in callback";
}

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad
{
    [super viewDidLoad];

  base::MessageLoopForUI* message_loop = new base::MessageLoopForUI;
  message_loop->Attach();
  base::MessageLoop::current()->PostTask(FROM_HERE, base::Bind(&DoSomething));
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end

