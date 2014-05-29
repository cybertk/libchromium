//
//  rest_request_context_getter.cc
//  libchromium-demo
//
//  Created by Quanlong He on 5/30/14.
//  Copyright (c) 2014 Quanlong He. All rights reserved.
//

#include "rest_request_context_getter.h"

#include "base/logging.h"
#include "base/path_service.h"
#include "base/single_thread_task_runner.h"
#include "net/url_request/url_request_context.h"
#include "net/url_request/url_request_context_builder.h"
#include "net/url_request/url_request_context_getter.h"

namespace rest {

namespace {
  scoped_refptr<net::URLRequestContextGetter> g_request_context_getter = NULL;
}

RestRequestContextGetter::RestRequestContextGetter(
    const scoped_refptr<base::SingleThreadTaskRunner>& task_runner)
    : builder_(new net::URLRequestContextBuilder),
      task_runner_(task_runner) {
  DCHECK(task_runner_);
}

RestRequestContextGetter::~RestRequestContextGetter() {
}

// static
net::URLRequestContextGetter* RestRequestContextGetter::Get() {
  return g_request_context_getter.get();
}

// static
void RestRequestContextGetter::Create(
         const scoped_refptr<base::MessageLoopProxy>& message_loop) {
  if (g_request_context_getter == NULL) {
    g_request_context_getter = new RestRequestContextGetter(message_loop);
  }
}

net::URLRequestContext* RestRequestContextGetter::GetURLRequestContext() {
  if (context_ == NULL) {
    net::URLRequestContextBuilder::HttpCacheParams cache_params;
    // Use max cache size of 256M
    cache_params.max_size = 256 * 1024 * 1024;
    cache_params.type = net::URLRequestContextBuilder::HttpCacheParams::DISK;
    base::FilePath cache_path;
    //PathService::Get(rest::DIR_REST_CACHE, &cache_path);
    cache_params.path = cache_path;
    builder_->EnableHttpCache(cache_params);
    context_.reset(builder_->Build());
  }
  return context_.get();
}

scoped_refptr<base::SingleThreadTaskRunner>
RestRequestContextGetter::GetNetworkTaskRunner() const {
  return task_runner_;
}

}  // namespace rest
