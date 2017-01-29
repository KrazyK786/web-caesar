#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, cgi
import caesar

def build_page(textarea_content):
    rot_label = "<label>Rotate by:</label>"

    rotation_input = "<input type='number' name='rotation'/>"

    message_label = "<label>Type a message:</label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    submit = "<input type='submit' >"
    form = "<form method='post'>" + rot_label + rotation_input + "<br><br>" + message_label + textarea  + "<br>" + submit + "</form>"

    head = """
    <head>
        <title>Web Caesar</title>
        <style type="text/css">
            .error{
                color:red;
            }
        </style>
    </head>
    """

    header = "<h2>Web Caesar</h2>"

    return head + header + form

def errorElement(error):

    error_element = "<p class='error'>" + error + "</p>" if error else ""

    return error_element


class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")

        error = self.request.get("error")
        error_element = errorElement(error) #"<p class='error'>" + error + "</p>" if error else ""

        self.response.write(content + error_element)

    def post(self):
        message = self.request.get("message")

        if not self.request.get("rotation"):
            error = "Please enter an amount to rotate by"

            error_element = errorElement(error) # "<p class='error'>" + error + "</p>" if error else ""
            content = build_page(message)
            self.response.write(content + error_element)
            #self.redirect("/?error=" + error)
        else:
            error = ""

            escaped_message = cgi.escape(message)

            encrypted_message = caesar.encrypt(escaped_message, int(self.request.get("rotation")))

            content = build_page(encrypted_message)

            self.response.write(content + error)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
