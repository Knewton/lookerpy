# coding: utf-8

"""
LookApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient
from .connect_to_api import connect_to_api



class LookApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

        # When instantiating this class, get an access token and store it as an instance variable
        __access_token = connect_to_api()
        self.__access_token = __access_token

    def all_looks(self, **kwargs):
        """
        get all looks
        ### Get all the looks.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.all_looks(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str fields: Requested fields.
        :return: list[Look]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['fields']
        all_params.append('callback')

        params = dir(self)

        query_params = {}
        if 'client_id' in params:
            query_params['client_id'] = self.client_id
        if 'client_secret' in params:
            query_params['client_secret'] = self.client_secret

        resource_path = '/looks'.replace('{format}', 'json')

        path_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # We put the access token on the instance in the header of our request.
        header_params['Authorization'] = 'token ' + self.__access_token

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Look]')
        return response

    def create_look_prefetch(self, look_id, **kwargs):
        """
        create a prefetch
        ### Create a prefetch for a look with the specified information. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_look_prefetch(look_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str look_id: Id of dashboard (required)
        :param PrefetchLookRequestMapper body: Parameters for prefetch request
        :return: PrefetchLookRequestMapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id', 'body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_look_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'look_id' is set
        if ('look_id' not in params) or (params['look_id'] is None):
            raise ValueError(
                "Missing the required parameter `look_id` when calling `create_look_prefetch`")

        resource_path = '/looks/{look_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchLookRequestMapper',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def look(self, look_id, **kwargs):
        """
        get look
        ### Get a Look.  Return detailed information about the Look and its associated Query.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.look(look_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int look_id: Id of look (required)
        :param str fields: Requested fields.
        :return: LookWithQuery
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id', 'fields']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method look" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'look_id' is set
        if ('look_id' not in params) or (params['look_id'] is None):
            raise ValueError("Missing the required parameter `look_id` when calling `look`")

        resource_path = '/looks/{look_id}'.replace('{format}', 'json')
        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']

        query_params = {}
        if 'client_id' in params:
            query_params['client_id'] = params['client_id']
        if 'client_secret' in params:
            query_params['client_secret'] = params['client_secret']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='LookWithQuery',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def look_prefetch(self, look_id, **kwargs):
        """
        get a prefetch
        ### Get a prefetch for a look with the specified information. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.look_prefetch(look_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str look_id: Id of look (required)
        :return: PrefetchMapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method look_prefetch" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'look_id' is set
        if ('look_id' not in params) or (params['look_id'] is None):
            raise ValueError(
                "Missing the required parameter `look_id` when calling `look_prefetch`")

        resource_path = '/looks/{look_id}/prefetch'.replace('{format}', 'json')
        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='PrefetchMapper',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def run_look(self, look_id, format, **kwargs):
        """
        run look
        ### Run a Look.  Given a look id and a format, this will run the look's query and return the results.  Suported formats: - json - plain json - csv - comma separated values with a header - txt - tab separated values with a header - html - simple html - md - simple markdown - sql - shows the generated SQL rather than running the query - png - a PNG image of the visualization of the query - jpg - a JPG image of the visualization of the query - unified - json that is annotated with additional metadata as used by the Looker web application   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.run_look(look_id, format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int look_id: Id of look (required)
        :param str format: Format of result (required)
        :param int limit: Row limit (may override the limit in the saved query).
        :param bool apply_formatting: Apply model-specified formatting to each result.
        :param bool cache: Get results from cache if available.
        :param int image_width: Render width for image formats.
        :param int image_height: Render height for image formats.
        :param bool generate_drill_links: Generate drill links (only applicable to 'unified' format.
        :param bool force_production: Force use of production models even if the user is in developer mode.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id', 'format', 'limit', 'apply_formatting', 'cache', 'image_width',
                      'image_height', 'generate_drill_links', 'force_production']
        all_params.append('callback')
        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_look" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'look_id' is set
        if ('look_id' not in params) or (params['look_id'] is None):
            raise ValueError("Missing the required parameter `look_id` when calling `run_look`")
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `run_look`")

        resource_path = '/looks/{look_id}/run/{format}'

        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']
        if 'format' in params:
            path_params['format'] = params['format']

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'apply_formatting' in params:
            query_params['apply_formatting'] = params['apply_formatting']
        if 'cache' in params:
            query_params['cache'] = params['cache']
        if 'image_width' in params:
            query_params['image_width'] = params['image_width']
        if 'image_height' in params:
            query_params['image_height'] = params['image_height']
        if 'generate_drill_links' in params:
            query_params['generate_drill_links'] = params['generate_drill_links']
        if 'force_production' in params:
            query_params['force_production'] = params['force_production']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client. \
            select_header_accept(['text', 'application/json', 'image/png', 'image/jpg'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client. \
            select_header_content_type(['application/json'])

        # We put the access token on the instance in the header of our request.
        header_params['Authorization'] = 'token ' + self.__access_token

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            callback=params.get('callback'))

        return response
