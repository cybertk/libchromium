//
//  rest_request_context_getter.h
//  libchromium-demo
//
//  Created by Quanlong He on 5/30/14.
//  Copyright (c) 2014 Quanlong He. All rights reserved.
//

#ifndef SERVERAGENT_REST_REQUEST_CONTEXT_GETTER_H_
#define SERVERAGENT_REST_REQUEST_CONTEXT_GETTER_H_

#include "net/url_request/url_request_context_getter.h"
#include "base/message_loop/message_loop_proxy.h"
#include "base/memory/scoped_ptr.h"
#include "base/memory/ref_counted.h"

namespace net {
class URLRequestContext;
class URLRequestContextBuilder;
}

namespace base {
class SingleThreadTaskRunner;
}

namespace rest {

// This class realize the interface of URLRequestContextGetter
// Used to return a dummy context, which lives on the message loop
// given in the constructor.
class RestRequestContextGetter : public net::URLRequestContextGetter {
 public:
  // |task_runner| must not be NULL.
  explicit RestRequestContextGetter(
      const scoped_refptr<base::SingleThreadTaskRunner>& task_runner);

  // URLRequestContextGetter implementation.
  virtual net::URLRequestContext* GetURLRequestContext() OVERRIDE;
  virtual scoped_refptr<base::SingleThreadTaskRunner>
      GetNetworkTaskRunner() const OVERRIDE;
  static net::URLRequestContextGetter* Get();
  static void Create(const scoped_refptr<base::MessageLoopProxy>& message_loop);

 private:
  // Only allow ourselves to be deleted by reference counting.
  virtual ~RestRequestContextGetter();
  scoped_ptr<net::URLRequestContext> context_;
  scoped_ptr<net::URLRequestContextBuilder> builder_;
  const scoped_refptr<base::SingleThreadTaskRunner> task_runner_;
};

}  // namespace rest

#endif  // SERVERAGENT_REST_REQUEST_CONTEXT_GETTER_H_
