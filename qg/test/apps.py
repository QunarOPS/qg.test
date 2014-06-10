# -*- coding: utf-8 -*-
#
# Copyright 2013, Qunar OPSDEV
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Author: jaypei <jaypei97159@gmail.com>
#


from qg.web.app import QWsgiApplication
from webtest import TestApp


def test_wsgi_app(app):
    assert(isinstance(app, QWsgiApplication))
    app._step_invoke("configure")
    app._step_invoke("run", do_pre=True, do_fn=False, do_post=False)
    return TestApp(app.wsgi_app)
