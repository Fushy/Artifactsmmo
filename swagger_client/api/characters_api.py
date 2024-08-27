# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json   # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CharactersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_character_characters_create_post(self, body, **kwargs):  # noqa: E501
        """Create Character  # noqa: E501

        Create new character on your account. You can create up to 5 characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_character_characters_create_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCharacterSchema body: (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_character_characters_create_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_character_characters_create_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_character_characters_create_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Character  # noqa: E501

        Create new character on your account. You can create up to 5 characters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_character_characters_create_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AddCharacterSchema body: (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_character_characters_create_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_character_characters_create_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWTBearer']  # noqa: E501

        return self.api_client.call_api(
            '/characters/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CharacterResponseSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_character_characters_delete_post(self, body, **kwargs):  # noqa: E501
        """Delete Character  # noqa: E501

        Delete character on your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_character_characters_delete_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteCharacterSchema body: (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_character_characters_delete_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_character_characters_delete_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def delete_character_characters_delete_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete Character  # noqa: E501

        Delete character on your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_character_characters_delete_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteCharacterSchema body: (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_character_characters_delete_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_character_characters_delete_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['JWTBearer']  # noqa: E501

        return self.api_client.call_api(
            '/characters/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CharacterResponseSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_characters_characters_get(self, **kwargs):  # noqa: E501
        """Get All Characters  # noqa: E501

        Fetch characters details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_characters_characters_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number
        :param object size: Page size
        :return: DataPageCharacterSchema_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_characters_characters_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_characters_characters_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_characters_characters_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get All Characters  # noqa: E501

        Fetch characters details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_characters_characters_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object page: Page number
        :param object size: Page size
        :return: DataPageCharacterSchema_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_characters_characters_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/characters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataPageCharacterSchema_',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_character_achievements_characters_name_achievements_get(self, name, **kwargs):  # noqa: E501
        """Get Character Achievements  # noqa: E501

        Retrieve the details of a character.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_character_achievements_characters_name_achievements_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: The character name. (required)
        :param object type: Type of achievements.
        :param object completed: Filter by completed achievements.
        :param object page: Page number
        :param object size: Page size
        :return: DataPageAchievementSchema_
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_character_achievements_characters_name_achievements_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_character_achievements_characters_name_achievements_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_character_achievements_characters_name_achievements_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get Character Achievements  # noqa: E501

        Retrieve the details of a character.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_character_achievements_characters_name_achievements_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: The character name. (required)
        :param object type: Type of achievements.
        :param object completed: Filter by completed achievements.
        :param object page: Page number
        :param object size: Page size
        :return: DataPageAchievementSchema_
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'type', 'completed', 'page', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_character_achievements_characters_name_achievements_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_character_achievements_characters_name_achievements_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'completed' in params:
            query_params.append(('completed', params['completed']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/characters/{name}/achievements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataPageAchievementSchema_',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_character_characters_name_get(self, name, **kwargs):  # noqa: E501
        """Get Character  # noqa: E501

        Retrieve the details of a character.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_character_characters_name_get(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: The character name. (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_character_characters_name_get_with_http_info(name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_character_characters_name_get_with_http_info(name, **kwargs)  # noqa: E501
            return data

    def get_character_characters_name_get_with_http_info(self, name, **kwargs):  # noqa: E501
        """Get Character  # noqa: E501

        Retrieve the details of a character.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_character_characters_name_get_with_http_info(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object name: The character name. (required)
        :return: CharacterResponseSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_character_characters_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_character_characters_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/characters/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CharacterResponseSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
