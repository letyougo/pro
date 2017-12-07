webpackJsonp([3],{

/***/ "+GGk":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

function InterceptorManager() {
  this.handlers = [];
}

/**
 * Add a new interceptor to the stack
 *
 * @param {Function} fulfilled The function to handle `then` for a `Promise`
 * @param {Function} rejected The function to handle `reject` for a `Promise`
 *
 * @return {Number} An ID used to remove interceptor later
 */
InterceptorManager.prototype.use = function use(fulfilled, rejected) {
  this.handlers.push({
    fulfilled: fulfilled,
    rejected: rejected
  });
  return this.handlers.length - 1;
};

/**
 * Remove an interceptor from the stack
 *
 * @param {Number} id The ID that was returned by `use`
 */
InterceptorManager.prototype.eject = function eject(id) {
  if (this.handlers[id]) {
    this.handlers[id] = null;
  }
};

/**
 * Iterate over all the registered interceptors
 *
 * This method is particularly useful for skipping over any
 * interceptors that may have become `null` calling `eject`.
 *
 * @param {Function} fn The function to call for each interceptor
 */
InterceptorManager.prototype.forEach = function forEach(fn) {
  utils.forEach(this.handlers, function forEachHandler(h) {
    if (h !== null) {
      fn(h);
    }
  });
};

module.exports = InterceptorManager;


/***/ }),

/***/ "/VWB":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var Cancel = __webpack_require__("RlDD");

/**
 * A `CancelToken` is an object that can be used to request cancellation of an operation.
 *
 * @class
 * @param {Function} executor The executor function.
 */
function CancelToken(executor) {
  if (typeof executor !== 'function') {
    throw new TypeError('executor must be a function.');
  }

  var resolvePromise;
  this.promise = new Promise(function promiseExecutor(resolve) {
    resolvePromise = resolve;
  });

  var token = this;
  executor(function cancel(message) {
    if (token.reason) {
      // Cancellation has already been requested
      return;
    }

    token.reason = new Cancel(message);
    resolvePromise(token.reason);
  });
}

/**
 * Throws a `Cancel` if cancellation has been requested.
 */
CancelToken.prototype.throwIfRequested = function throwIfRequested() {
  if (this.reason) {
    throw this.reason;
  }
};

/**
 * Returns an object that contains a new `CancelToken` and a function that, when called,
 * cancels the `CancelToken`.
 */
CancelToken.source = function source() {
  var cancel;
  var token = new CancelToken(function executor(c) {
    cancel = c;
  });
  return {
    token: token,
    cancel: cancel
  };
};

module.exports = CancelToken;


/***/ }),

/***/ "0l+G":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var enhanceError = __webpack_require__("obgR");

/**
 * Create an Error with the specified message, config, error code, request and response.
 *
 * @param {string} message The error message.
 * @param {Object} config The config.
 * @param {string} [code] The error code (for example, 'ECONNABORTED').
 * @param {Object} [request] The request.
 * @param {Object} [response] The response.
 * @returns {Error} The created error.
 */
module.exports = function createError(message, config, code, request, response) {
  var error = new Error(message);
  return enhanceError(error, config, code, request, response);
};


/***/ }),

/***/ "1DmB":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

module.exports = (
  utils.isStandardBrowserEnv() ?

  // Standard browser envs have full support of the APIs needed to test
  // whether the request URL is of the same origin as current location.
  (function standardBrowserEnv() {
    var msie = /(msie|trident)/i.test(navigator.userAgent);
    var urlParsingNode = document.createElement('a');
    var originURL;

    /**
    * Parse a URL to discover it's components
    *
    * @param {String} url The URL to be parsed
    * @returns {Object}
    */
    function resolveURL(url) {
      var href = url;

      if (msie) {
        // IE needs attribute set twice to normalize properties
        urlParsingNode.setAttribute('href', href);
        href = urlParsingNode.href;
      }

      urlParsingNode.setAttribute('href', href);

      // urlParsingNode provides the UrlUtils interface - http://url.spec.whatwg.org/#urlutils
      return {
        href: urlParsingNode.href,
        protocol: urlParsingNode.protocol ? urlParsingNode.protocol.replace(/:$/, '') : '',
        host: urlParsingNode.host,
        search: urlParsingNode.search ? urlParsingNode.search.replace(/^\?/, '') : '',
        hash: urlParsingNode.hash ? urlParsingNode.hash.replace(/^#/, '') : '',
        hostname: urlParsingNode.hostname,
        port: urlParsingNode.port,
        pathname: (urlParsingNode.pathname.charAt(0) === '/') ?
                  urlParsingNode.pathname :
                  '/' + urlParsingNode.pathname
      };
    }

    originURL = resolveURL(window.location.href);

    /**
    * Determine if a URL shares the same origin as the current location
    *
    * @param {String} requestURL The URL to test
    * @returns {boolean} True if URL shares the same origin, otherwise false
    */
    return function isURLSameOrigin(requestURL) {
      var parsed = (utils.isString(requestURL)) ? resolveURL(requestURL) : requestURL;
      return (parsed.protocol === originURL.protocol &&
            parsed.host === originURL.host);
    };
  })() :

  // Non standard browser envs (web workers, react-native) lack needed support.
  (function nonStandardBrowserEnv() {
    return function isURLSameOrigin() {
      return true;
    };
  })()
);


/***/ }),

/***/ "4nb4":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


module.exports = function bind(fn, thisArg) {
  return function wrap() {
    var args = new Array(arguments.length);
    for (var i = 0; i < args.length; i++) {
      args[i] = arguments[i];
    }
    return fn.apply(thisArg, args);
  };
};


/***/ }),

/***/ "5IMM":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator__ = __webpack_require__("Xxa5");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator__ = __webpack_require__("exGp");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__node_modules_element_ui_packages_button_src_button_group_vue__ = __webpack_require__("RvCN");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__config__ = __webpack_require__("iOPO");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__node_modules_element_ui_packages_button_src_button_vue__ = __webpack_require__("EMXe");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__node_modules_element_ui_packages_form_src_form_vue__ = __webpack_require__("xrpo");


//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//







/* harmony default export */ __webpack_exports__["a"] = ({
  components: {
    ElForm: __WEBPACK_IMPORTED_MODULE_5__node_modules_element_ui_packages_form_src_form_vue__["a" /* default */],
    ElButton: __WEBPACK_IMPORTED_MODULE_4__node_modules_element_ui_packages_button_src_button_vue__["a" /* default */],
    ElButtonGroup: __WEBPACK_IMPORTED_MODULE_2__node_modules_element_ui_packages_button_src_button_group_vue__["a" /* default */] },
  name: 'office',
  data: function data() {
    return {
      school_id: window.school_id,
      list: [],
      total: 0,
      search: '',
      page_size: 10,
      current_page: 1,
      loading: false,
      add_form: {
        office_name: '',
        exam_name: '',
        register_username: "",
        register_password: '',
        visible: false

      },
      edit_form: {
        id: '',
        office_name: '',
        exam_name: '',
        register_userid: '',
        register_username: '',
        register_password: '',
        visible: false,
        change_password: false
      },
      upload_dialog: {
        visible: false
      }
    };
  },


  watch: {
    current_page: function current_page() {
      this.fetch();
    }
  },

  methods: {
    change_page: function change_page(p) {
      console.log(p);
    },
    open_edit: function open_edit(data) {
      console.log(data);
      var change_password = this.edit_form.change_password;
      data.visible = true;
      this.edit_form = {
        visible: true,
        id: data.id,
        office_name: data.office_name,
        exam_name: data.exam_name,
        register_userid: data.register_userid,
        register_username: data.register_username,
        register_password: data.register_password,
        change_password: change_password
      };
    },
    fetch: function fetch() {
      var _this = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee() {
        var _limit, _page, search, that, response;

        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee$(_context) {
          while (1) {
            switch (_context.prev = _context.next) {
              case 0:
                _limit = _this.page_size, _page = _this.current_page, search = _this.search, that = _this;


                _this.loading = true;

                _context.next = 4;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].get('/api/office/');

              case 4:
                response = _context.sent;

                _this.list = response.data.objects;

                _this.loading = false;

              case 7:
              case "end":
                return _context.stop();
            }
          }
        }, _callee, _this);
      }))();
    },
    add: function add() {
      var _this2 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee2() {
        var add_form, response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee2$(_context2) {
          while (1) {
            switch (_context2.prev = _context2.next) {
              case 0:
                add_form = _this2.add_form;


                console.log(add_form, '----');

                _context2.next = 4;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].post('/api/office/', add_form);

              case 4:
                response = _context2.sent;

                _this2.add_form.visible = false;
                _this2.fetch();

              case 7:
              case "end":
                return _context2.stop();
            }
          }
        }, _callee2, _this2);
      }))();
    },
    remove: function remove(data) {
      var _this3 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee3() {
        var response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee3$(_context3) {
          while (1) {
            switch (_context3.prev = _context3.next) {
              case 0:
                _context3.prev = 0;
                _context3.next = 3;
                return _this3.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                });

              case 3:
                _context3.next = 5;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].delete('/api/office/' + data.id + '/');

              case 5:
                response = _context3.sent;


                _this3.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                _this3.fetch();
                _context3.next = 13;
                break;

              case 10:
                _context3.prev = 10;
                _context3.t0 = _context3["catch"](0);

                _this3.$message({
                  type: 'info',
                  message: '已取消删除'
                });

              case 13:
              case "end":
                return _context3.stop();
            }
          }
        }, _callee3, _this3, [[0, 10]]);
      }))();
    },
    edit: function edit() {
      var _this4 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee4() {
        var edit_form, id, response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee4$(_context4) {
          while (1) {
            switch (_context4.prev = _context4.next) {
              case 0:
                edit_form = _this4.edit_form;

                console.log(edit_form);
                id = edit_form.id;


                _this4.$message({
                  type: 'success',
                  message: '修改信息成功!'
                });

                _context4.next = 6;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].put('/api/office/' + id + '/', edit_form);

              case 6:
                response = _context4.sent;

                _this4.edit_form.visible = false;
                _this4.fetch();

              case 9:
              case "end":
                return _context4.stop();
            }
          }
        }, _callee4, _this4);
      }))();
    }
  },
  mounted: function mounted() {

    this.fetch();
  }
});

/***/ }),

/***/ "5aBc":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


// btoa polyfill for IE<10 courtesy https://github.com/davidchambers/Base64.js

var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';

function E() {
  this.message = 'String contains an invalid character';
}
E.prototype = new Error;
E.prototype.code = 5;
E.prototype.name = 'InvalidCharacterError';

function btoa(input) {
  var str = String(input);
  var output = '';
  for (
    // initialize result and counter
    var block, charCode, idx = 0, map = chars;
    // if the next str index does not exist:
    //   change the mapping table to "="
    //   check if d has no fractional digits
    str.charAt(idx | 0) || (map = '=', idx % 1);
    // "8 - idx % 1 * 8" generates the sequence 2, 4, 6, 8
    output += map.charAt(63 & block >> 8 - idx % 1 * 8)
  ) {
    charCode = str.charCodeAt(idx += 3 / 4);
    if (charCode > 0xFF) {
      throw new E();
    }
    block = block << 8 | charCode;
  }
  return output;
}

module.exports = btoa;


/***/ }),

/***/ "5ovs":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__("7+uW");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__App__ = __webpack_require__("WzdC");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__router__ = __webpack_require__("oaLO");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_element_ui__ = __webpack_require__("zL8q");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3_element_ui___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_3_element_ui__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_element_ui_lib_theme_chalk_index_css__ = __webpack_require__("tvR6");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4_element_ui_lib_theme_chalk_index_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_4_element_ui_lib_theme_chalk_index_css__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__index_css__ = __webpack_require__("lv6U");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__index_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_5__index_css__);
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.





__WEBPACK_IMPORTED_MODULE_0_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_3_element_ui___default.a)
__WEBPACK_IMPORTED_MODULE_0_vue__["default"].config.productionTip = false

/* eslint-disable no-new */


new __WEBPACK_IMPORTED_MODULE_0_vue__["default"]({
  el: '#app',
  router: __WEBPACK_IMPORTED_MODULE_2__router__["a" /* default */],
  template: '<App/>',
  components: { App: __WEBPACK_IMPORTED_MODULE_1__App__["a" /* default */] }
})


/***/ }),

/***/ "7LYE":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");
var settle = __webpack_require__("wZW9");
var buildURL = __webpack_require__("RS1v");
var parseHeaders = __webpack_require__("9T8H");
var isURLSameOrigin = __webpack_require__("1DmB");
var createError = __webpack_require__("0l+G");
var btoa = (typeof window !== 'undefined' && window.btoa && window.btoa.bind(window)) || __webpack_require__("5aBc");

module.exports = function xhrAdapter(config) {
  return new Promise(function dispatchXhrRequest(resolve, reject) {
    var requestData = config.data;
    var requestHeaders = config.headers;

    if (utils.isFormData(requestData)) {
      delete requestHeaders['Content-Type']; // Let the browser set it
    }

    var request = new XMLHttpRequest();
    var loadEvent = 'onreadystatechange';
    var xDomain = false;

    // For IE 8/9 CORS support
    // Only supports POST and GET calls and doesn't returns the response headers.
    // DON'T do this for testing b/c XMLHttpRequest is mocked, not XDomainRequest.
    if ("production" !== 'test' &&
        typeof window !== 'undefined' &&
        window.XDomainRequest && !('withCredentials' in request) &&
        !isURLSameOrigin(config.url)) {
      request = new window.XDomainRequest();
      loadEvent = 'onload';
      xDomain = true;
      request.onprogress = function handleProgress() {};
      request.ontimeout = function handleTimeout() {};
    }

    // HTTP basic authentication
    if (config.auth) {
      var username = config.auth.username || '';
      var password = config.auth.password || '';
      requestHeaders.Authorization = 'Basic ' + btoa(username + ':' + password);
    }

    request.open(config.method.toUpperCase(), buildURL(config.url, config.params, config.paramsSerializer), true);

    // Set the request timeout in MS
    request.timeout = config.timeout;

    // Listen for ready state
    request[loadEvent] = function handleLoad() {
      if (!request || (request.readyState !== 4 && !xDomain)) {
        return;
      }

      // The request errored out and we didn't get a response, this will be
      // handled by onerror instead
      // With one exception: request that using file: protocol, most browsers
      // will return status as 0 even though it's a successful request
      if (request.status === 0 && !(request.responseURL && request.responseURL.indexOf('file:') === 0)) {
        return;
      }

      // Prepare the response
      var responseHeaders = 'getAllResponseHeaders' in request ? parseHeaders(request.getAllResponseHeaders()) : null;
      var responseData = !config.responseType || config.responseType === 'text' ? request.responseText : request.response;
      var response = {
        data: responseData,
        // IE sends 1223 instead of 204 (https://github.com/axios/axios/issues/201)
        status: request.status === 1223 ? 204 : request.status,
        statusText: request.status === 1223 ? 'No Content' : request.statusText,
        headers: responseHeaders,
        config: config,
        request: request
      };

      settle(resolve, reject, response);

      // Clean up request
      request = null;
    };

    // Handle low level network errors
    request.onerror = function handleError() {
      // Real errors are hidden from us by the browser
      // onerror should only fire if it's a network error
      reject(createError('Network Error', config, null, request));

      // Clean up request
      request = null;
    };

    // Handle timeout
    request.ontimeout = function handleTimeout() {
      reject(createError('timeout of ' + config.timeout + 'ms exceeded', config, 'ECONNABORTED',
        request));

      // Clean up request
      request = null;
    };

    // Add xsrf header
    // This is only done if running in a standard browser environment.
    // Specifically not if we're in a web worker, or react-native.
    if (utils.isStandardBrowserEnv()) {
      var cookies = __webpack_require__("OhlP");

      // Add xsrf header
      var xsrfValue = (config.withCredentials || isURLSameOrigin(config.url)) && config.xsrfCookieName ?
          cookies.read(config.xsrfCookieName) :
          undefined;

      if (xsrfValue) {
        requestHeaders[config.xsrfHeaderName] = xsrfValue;
      }
    }

    // Add headers to the request
    if ('setRequestHeader' in request) {
      utils.forEach(requestHeaders, function setRequestHeader(val, key) {
        if (typeof requestData === 'undefined' && key.toLowerCase() === 'content-type') {
          // Remove Content-Type if data is undefined
          delete requestHeaders[key];
        } else {
          // Otherwise add header to the request
          request.setRequestHeader(key, val);
        }
      });
    }

    // Add withCredentials to request if needed
    if (config.withCredentials) {
      request.withCredentials = true;
    }

    // Add responseType to request if needed
    if (config.responseType) {
      try {
        request.responseType = config.responseType;
      } catch (e) {
        // Expected DOMException thrown by browsers not compatible XMLHttpRequest Level 2.
        // But, this can be suppressed for 'json' type as it can be parsed by default 'transformResponse' function.
        if (config.responseType !== 'json') {
          throw e;
        }
      }
    }

    // Handle progress if needed
    if (typeof config.onDownloadProgress === 'function') {
      request.addEventListener('progress', config.onDownloadProgress);
    }

    // Not all browsers support upload events
    if (typeof config.onUploadProgress === 'function' && request.upload) {
      request.upload.addEventListener('progress', config.onUploadProgress);
    }

    if (config.cancelToken) {
      // Handle cancellation
      config.cancelToken.promise.then(function onCanceled(cancel) {
        if (!request) {
          return;
        }

        request.abort();
        reject(cancel);
        // Clean up request
        request = null;
      });
    }

    if (requestData === undefined) {
      requestData = null;
    }

    // Send the request
    request.send(requestData);
  });
};


/***/ }),

/***/ "8s4O":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["a"] = ({
  name: 'ElButton',

  inject: {
    elFormItem: {
      default: ''
    }
  },

  props: {
    type: {
      type: String,
      default: 'default'
    },
    size: String,
    icon: {
      type: String,
      default: ''
    },
    nativeType: {
      type: String,
      default: 'button'
    },
    loading: Boolean,
    disabled: Boolean,
    plain: Boolean,
    autofocus: Boolean,
    round: Boolean
  },

  computed: {
    _elFormItemSize: function _elFormItemSize() {
      return (this.elFormItem || {}).elFormItemSize;
    },
    buttonSize: function buttonSize() {
      return this.size || this._elFormItemSize || (this.$ELEMENT || {}).size;
    }
  },

  methods: {
    handleClick: function handleClick(evt) {
      this.$emit('click', evt);
    },
    handleInnerClick: function handleInnerClick(evt) {
      if (this.disabled) {
        evt.stopPropagation();
      }
    }
  }
});

/***/ }),

/***/ "9RB6":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var defaults = __webpack_require__("T2kP");
var utils = __webpack_require__("zIVT");
var InterceptorManager = __webpack_require__("+GGk");
var dispatchRequest = __webpack_require__("U2+V");

/**
 * Create a new instance of Axios
 *
 * @param {Object} instanceConfig The default config for the instance
 */
function Axios(instanceConfig) {
  this.defaults = instanceConfig;
  this.interceptors = {
    request: new InterceptorManager(),
    response: new InterceptorManager()
  };
}

/**
 * Dispatch a request
 *
 * @param {Object} config The config specific for this request (merged with this.defaults)
 */
Axios.prototype.request = function request(config) {
  /*eslint no-param-reassign:0*/
  // Allow for axios('example/url'[, config]) a la fetch API
  if (typeof config === 'string') {
    config = utils.merge({
      url: arguments[0]
    }, arguments[1]);
  }

  config = utils.merge(defaults, this.defaults, { method: 'get' }, config);
  config.method = config.method.toLowerCase();

  // Hook up interceptors middleware
  var chain = [dispatchRequest, undefined];
  var promise = Promise.resolve(config);

  this.interceptors.request.forEach(function unshiftRequestInterceptors(interceptor) {
    chain.unshift(interceptor.fulfilled, interceptor.rejected);
  });

  this.interceptors.response.forEach(function pushResponseInterceptors(interceptor) {
    chain.push(interceptor.fulfilled, interceptor.rejected);
  });

  while (chain.length) {
    promise = promise.then(chain.shift(), chain.shift());
  }

  return promise;
};

// Provide aliases for supported request methods
utils.forEach(['delete', 'get', 'head', 'options'], function forEachMethodNoData(method) {
  /*eslint func-names:0*/
  Axios.prototype[method] = function(url, config) {
    return this.request(utils.merge(config || {}, {
      method: method,
      url: url
    }));
  };
});

utils.forEach(['post', 'put', 'patch'], function forEachMethodWithData(method) {
  /*eslint func-names:0*/
  Axios.prototype[method] = function(url, data, config) {
    return this.request(utils.merge(config || {}, {
      method: method,
      url: url,
      data: data
    }));
  };
});

module.exports = Axios;


/***/ }),

/***/ "9T8H":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

// Headers whose duplicates are ignored by node
// c.f. https://nodejs.org/api/http.html#http_message_headers
var ignoreDuplicateOf = [
  'age', 'authorization', 'content-length', 'content-type', 'etag',
  'expires', 'from', 'host', 'if-modified-since', 'if-unmodified-since',
  'last-modified', 'location', 'max-forwards', 'proxy-authorization',
  'referer', 'retry-after', 'user-agent'
];

/**
 * Parse headers into an object
 *
 * ```
 * Date: Wed, 27 Aug 2014 08:58:49 GMT
 * Content-Type: application/json
 * Connection: keep-alive
 * Transfer-Encoding: chunked
 * ```
 *
 * @param {String} headers Headers needing to be parsed
 * @returns {Object} Headers parsed into an object
 */
module.exports = function parseHeaders(headers) {
  var parsed = {};
  var key;
  var val;
  var i;

  if (!headers) { return parsed; }

  utils.forEach(headers.split('\n'), function parser(line) {
    i = line.indexOf(':');
    key = utils.trim(line.substr(0, i)).toLowerCase();
    val = utils.trim(line.substr(i + 1));

    if (key) {
      if (parsed[key] && ignoreDuplicateOf.indexOf(key) >= 0) {
        return;
      }
      if (key === 'set-cookie') {
        parsed[key] = (parsed[key] ? parsed[key] : []).concat([val]);
      } else {
        parsed[key] = parsed[key] ? parsed[key] + ', ' + val : val;
      }
    }
  });

  return parsed;
};


/***/ }),

/***/ "A9Yy":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_office_vue__ = __webpack_require__("5IMM");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_37656234_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_office_vue__ = __webpack_require__("bwIi");
function injectStyle (ssrContext) {
  __webpack_require__("u6N1")
}
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = injectStyle
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_office_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_37656234_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_office_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "AZqh":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "BTlr":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * Creates a new URL by combining the specified URLs
 *
 * @param {string} baseURL The base URL
 * @param {string} relativeURL The relative URL
 * @returns {string} The combined URL
 */
module.exports = function combineURLs(baseURL, relativeURL) {
  return relativeURL
    ? baseURL.replace(/\/+$/, '') + '/' + relativeURL.replace(/^\/+/, '')
    : baseURL;
};


/***/ }),

/***/ "C9l1":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


module.exports = function isCancel(value) {
  return !!(value && value.__CANCEL__);
};


/***/ }),

/***/ "EMXe":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_button_vue__ = __webpack_require__("8s4O");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_7dc2ea35_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_button_vue__ = __webpack_require__("Pbh3");
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = null
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_button_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_7dc2ea35_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_button_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "Ex+b":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * Determines whether the specified URL is absolute
 *
 * @param {string} url The URL to test
 * @returns {boolean} True if the specified URL is absolute, otherwise false
 */
module.exports = function isAbsoluteURL(url) {
  // A URL is considered absolute if it begins with "<scheme>://" or "//" (protocol-relative URL).
  // RFC 3986 defines scheme name as a sequence of characters beginning with a letter and followed
  // by any combination of letters, digits, plus, period, or hyphen.
  return /^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(url);
};


/***/ }),

/***/ "HXpE":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");
var bind = __webpack_require__("4nb4");
var Axios = __webpack_require__("9RB6");
var defaults = __webpack_require__("T2kP");

/**
 * Create an instance of Axios
 *
 * @param {Object} defaultConfig The default config for the instance
 * @return {Axios} A new instance of Axios
 */
function createInstance(defaultConfig) {
  var context = new Axios(defaultConfig);
  var instance = bind(Axios.prototype.request, context);

  // Copy axios.prototype to instance
  utils.extend(instance, Axios.prototype, context);

  // Copy context to instance
  utils.extend(instance, context);

  return instance;
}

// Create the default instance to be exported
var axios = createInstance(defaults);

// Expose Axios class to allow class inheritance
axios.Axios = Axios;

// Factory for creating new instances
axios.create = function create(instanceConfig) {
  return createInstance(utils.merge(defaults, instanceConfig));
};

// Expose Cancel & CancelToken
axios.Cancel = __webpack_require__("RlDD");
axios.CancelToken = __webpack_require__("/VWB");
axios.isCancel = __webpack_require__("C9l1");

// Expose all/spread
axios.all = function all(promises) {
  return Promise.all(promises);
};
axios.spread = __webpack_require__("Kbjq");

module.exports = axios;

// Allow use of default import syntax in TypeScript
module.exports.default = axios;


/***/ }),

/***/ "Jd6x":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{attrs:{"id":"app"}},[_c('div',{staticClass:"top-bar"},[_c('div',[_vm._v("考试管理系统-考试中心")]),_vm._v(" "),_c('div'),_vm._v(" "),_c('span',{staticClass:"name"},[_vm._v("欢迎："+_vm._s(_vm.user.name)),_c('a',{attrs:{"href":"/logout/"}},[_vm._v("退出")])])]),_vm._v(" "),_c('el-row',[_c('el-col',{attrs:{"span":2}},[_c('el-menu',{staticClass:"el-menu-vertical-demo",attrs:{"default-active":_vm.name}},[_c('el-menu-item',{attrs:{"index":"/school"},on:{"click":function($event){_vm.route('/school')}}},[_c('i',{staticClass:"el-icon-setting"}),_vm._v(" "),_c('span',{attrs:{"slot":"title"},slot:"title"},[_vm._v("学校")])]),_vm._v(" "),_c('el-menu-item',{attrs:{"index":"/office"},on:{"click":function($event){_vm.route('/office')}}},[_c('i',{staticClass:"el-icon-setting"}),_vm._v(" "),_c('span',{attrs:{"slot":"title"},slot:"title"},[_vm._v("考试办")])]),_vm._v(" "),_c('el-menu-item',{attrs:{"index":"/shui"},on:{"click":function($event){_vm.route('/shui')}}},[_c('i',{staticClass:"el-icon-setting"}),_vm._v(" "),_c('span',{attrs:{"slot":"title"},slot:"title"},[_vm._v("合并计税")])])],1)],1),_vm._v(" "),_c('el-col',{attrs:{"span":22}},[_c('router-view')],1)],1)],1)}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "Kbjq":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * Syntactic sugar for invoking a function and expanding an array for arguments.
 *
 * Common use case would be to use `Function.prototype.apply`.
 *
 *  ```js
 *  function f(x, y, z) {}
 *  var args = [1, 2, 3];
 *  f.apply(null, args);
 *  ```
 *
 * With `spread` this example can be re-written.
 *
 *  ```js
 *  spread(function(x, y, z) {})([1, 2, 3]);
 *  ```
 *
 * @param {Function} callback
 * @returns {Function}
 */
module.exports = function spread(callback) {
  return function wrap(arr) {
    return callback.apply(null, arr);
  };
};


/***/ }),

/***/ "NlYv":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "OhlP":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

module.exports = (
  utils.isStandardBrowserEnv() ?

  // Standard browser envs support document.cookie
  (function standardBrowserEnv() {
    return {
      write: function write(name, value, expires, path, domain, secure) {
        var cookie = [];
        cookie.push(name + '=' + encodeURIComponent(value));

        if (utils.isNumber(expires)) {
          cookie.push('expires=' + new Date(expires).toGMTString());
        }

        if (utils.isString(path)) {
          cookie.push('path=' + path);
        }

        if (utils.isString(domain)) {
          cookie.push('domain=' + domain);
        }

        if (secure === true) {
          cookie.push('secure');
        }

        document.cookie = cookie.join('; ');
      },

      read: function read(name) {
        var match = document.cookie.match(new RegExp('(^|;\\s*)(' + name + ')=([^;]*)'));
        return (match ? decodeURIComponent(match[3]) : null);
      },

      remove: function remove(name) {
        this.write(name, '', Date.now() - 86400000);
      }
    };
  })() :

  // Non standard browser env (web workers, react-native) lack needed support.
  (function nonStandardBrowserEnv() {
    return {
      write: function write() {},
      read: function read() { return null; },
      remove: function remove() {}
    };
  })()
);


/***/ }),

/***/ "Pbh3":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('button',{staticClass:"el-button",class:[
    _vm.type ? 'el-button--' + _vm.type : '',
    _vm.buttonSize ? 'el-button--' + _vm.buttonSize : '',
    {
      'is-disabled': _vm.disabled,
      'is-loading': _vm.loading,
      'is-plain': _vm.plain,
      'is-round': _vm.round
    }
  ],attrs:{"disabled":_vm.disabled,"autofocus":_vm.autofocus,"type":_vm.nativeType},on:{"click":_vm.handleClick}},[(_vm.loading)?_c('i',{staticClass:"el-icon-loading",on:{"click":_vm.handleInnerClick}}):_vm._e(),_vm._v(" "),(_vm.icon && !_vm.loading)?_c('i',{class:_vm.icon,on:{"click":_vm.handleInnerClick}}):_vm._e(),_vm._v(" "),(_vm.$slots.default)?_c('span',{on:{"click":_vm.handleInnerClick}},[_vm._t("default")],2):_vm._e()])}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "RS1v":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

function encode(val) {
  return encodeURIComponent(val).
    replace(/%40/gi, '@').
    replace(/%3A/gi, ':').
    replace(/%24/g, '$').
    replace(/%2C/gi, ',').
    replace(/%20/g, '+').
    replace(/%5B/gi, '[').
    replace(/%5D/gi, ']');
}

/**
 * Build a URL by appending params to the end
 *
 * @param {string} url The base of the url (e.g., http://www.google.com)
 * @param {object} [params] The params to be appended
 * @returns {string} The formatted url
 */
module.exports = function buildURL(url, params, paramsSerializer) {
  /*eslint no-param-reassign:0*/
  if (!params) {
    return url;
  }

  var serializedParams;
  if (paramsSerializer) {
    serializedParams = paramsSerializer(params);
  } else if (utils.isURLSearchParams(params)) {
    serializedParams = params.toString();
  } else {
    var parts = [];

    utils.forEach(params, function serialize(val, key) {
      if (val === null || typeof val === 'undefined') {
        return;
      }

      if (utils.isArray(val)) {
        key = key + '[]';
      }

      if (!utils.isArray(val)) {
        val = [val];
      }

      utils.forEach(val, function parseValue(v) {
        if (utils.isDate(v)) {
          v = v.toISOString();
        } else if (utils.isObject(v)) {
          v = JSON.stringify(v);
        }
        parts.push(encode(key) + '=' + encode(v));
      });
    });

    serializedParams = parts.join('&');
  }

  if (serializedParams) {
    url += (url.indexOf('?') === -1 ? '?' : '&') + serializedParams;
  }

  return url;
};


/***/ }),

/***/ "RlDD":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * A `Cancel` is an object that is thrown when an operation is canceled.
 *
 * @class
 * @param {string=} message The message.
 */
function Cancel(message) {
  this.message = message;
}

Cancel.prototype.toString = function toString() {
  return 'Cancel' + (this.message ? ': ' + this.message : '');
};

Cancel.prototype.__CANCEL__ = true;

module.exports = Cancel;


/***/ }),

/***/ "RvCN":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_button_group_vue__ = __webpack_require__("ZLW0");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_f386b308_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_button_group_vue__ = __webpack_require__("S+D4");
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = null
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_button_group_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_f386b308_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_button_group_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "S+D4":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"el-button-group"},[_vm._t("default")],2)}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "T2kP":
/***/ (function(module, exports, __webpack_require__) {

"use strict";
/* WEBPACK VAR INJECTION */(function(process) {

var utils = __webpack_require__("zIVT");
var normalizeHeaderName = __webpack_require__("TOXd");

var DEFAULT_CONTENT_TYPE = {
  'Content-Type': 'application/x-www-form-urlencoded'
};

function setContentTypeIfUnset(headers, value) {
  if (!utils.isUndefined(headers) && utils.isUndefined(headers['Content-Type'])) {
    headers['Content-Type'] = value;
  }
}

function getDefaultAdapter() {
  var adapter;
  if (typeof XMLHttpRequest !== 'undefined') {
    // For browsers use XHR adapter
    adapter = __webpack_require__("7LYE");
  } else if (typeof process !== 'undefined') {
    // For node use HTTP adapter
    adapter = __webpack_require__("7LYE");
  }
  return adapter;
}

var defaults = {
  adapter: getDefaultAdapter(),

  transformRequest: [function transformRequest(data, headers) {
    normalizeHeaderName(headers, 'Content-Type');
    if (utils.isFormData(data) ||
      utils.isArrayBuffer(data) ||
      utils.isBuffer(data) ||
      utils.isStream(data) ||
      utils.isFile(data) ||
      utils.isBlob(data)
    ) {
      return data;
    }
    if (utils.isArrayBufferView(data)) {
      return data.buffer;
    }
    if (utils.isURLSearchParams(data)) {
      setContentTypeIfUnset(headers, 'application/x-www-form-urlencoded;charset=utf-8');
      return data.toString();
    }
    if (utils.isObject(data)) {
      setContentTypeIfUnset(headers, 'application/json;charset=utf-8');
      return JSON.stringify(data);
    }
    return data;
  }],

  transformResponse: [function transformResponse(data) {
    /*eslint no-param-reassign:0*/
    if (typeof data === 'string') {
      try {
        data = JSON.parse(data);
      } catch (e) { /* Ignore */ }
    }
    return data;
  }],

  timeout: 0,

  xsrfCookieName: 'XSRF-TOKEN',
  xsrfHeaderName: 'X-XSRF-TOKEN',

  maxContentLength: -1,

  validateStatus: function validateStatus(status) {
    return status >= 200 && status < 300;
  }
};

defaults.headers = {
  common: {
    'Accept': 'application/json, text/plain, */*'
  }
};

utils.forEach(['delete', 'get', 'head'], function forEachMethodNoData(method) {
  defaults.headers[method] = {};
});

utils.forEach(['post', 'put', 'patch'], function forEachMethodWithData(method) {
  defaults.headers[method] = utils.merge(DEFAULT_CONTENT_TYPE);
});

module.exports = defaults;

/* WEBPACK VAR INJECTION */}.call(exports, __webpack_require__("W2nU")))

/***/ }),

/***/ "TOXd":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

module.exports = function normalizeHeaderName(headers, normalizedName) {
  utils.forEach(headers, function processHeader(value, name) {
    if (name !== normalizedName && name.toUpperCase() === normalizedName.toUpperCase()) {
      headers[normalizedName] = value;
      delete headers[name];
    }
  });
};


/***/ }),

/***/ "U2+V":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");
var transformData = __webpack_require__("i7gz");
var isCancel = __webpack_require__("C9l1");
var defaults = __webpack_require__("T2kP");
var isAbsoluteURL = __webpack_require__("Ex+b");
var combineURLs = __webpack_require__("BTlr");

/**
 * Throws a `Cancel` if cancellation has been requested.
 */
function throwIfCancellationRequested(config) {
  if (config.cancelToken) {
    config.cancelToken.throwIfRequested();
  }
}

/**
 * Dispatch a request to the server using the configured adapter.
 *
 * @param {object} config The config that is to be used for the request
 * @returns {Promise} The Promise to be fulfilled
 */
module.exports = function dispatchRequest(config) {
  throwIfCancellationRequested(config);

  // Support baseURL config
  if (config.baseURL && !isAbsoluteURL(config.url)) {
    config.url = combineURLs(config.baseURL, config.url);
  }

  // Ensure headers exist
  config.headers = config.headers || {};

  // Transform request data
  config.data = transformData(
    config.data,
    config.headers,
    config.transformRequest
  );

  // Flatten headers
  config.headers = utils.merge(
    config.headers.common || {},
    config.headers[config.method] || {},
    config.headers || {}
  );

  utils.forEach(
    ['delete', 'get', 'head', 'post', 'put', 'patch', 'common'],
    function cleanHeaderConfig(method) {
      delete config.headers[method];
    }
  );

  var adapter = config.adapter || defaults.adapter;

  return adapter(config).then(function onAdapterResolution(response) {
    throwIfCancellationRequested(config);

    // Transform response data
    response.data = transformData(
      response.data,
      response.headers,
      config.transformResponse
    );

    return response;
  }, function onAdapterRejection(reason) {
    if (!isCancel(reason)) {
      throwIfCancellationRequested(config);

      // Transform response data
      if (reason && reason.response) {
        reason.response.data = transformData(
          reason.response.data,
          reason.response.headers,
          config.transformResponse
        );
      }
    }

    return Promise.reject(reason);
  });
};


/***/ }),

/***/ "WzdC":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_App_vue__ = __webpack_require__("q8By");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_5208f121_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_App_vue__ = __webpack_require__("Jd6x");
function injectStyle (ssrContext) {
  __webpack_require__("NlYv")
}
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = injectStyle
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_App_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_5208f121_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_App_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "ZH5x":
/***/ (function(module, exports) {

/*!
 * Determine if an object is a Buffer
 *
 * @author   Feross Aboukhadijeh <feross@feross.org> <http://feross.org>
 * @license  MIT
 */

// The _isBuffer check is for Safari 5-7 support, because it's missing
// Object.prototype.constructor. Remove this eventually
module.exports = function (obj) {
  return obj != null && (isBuffer(obj) || isSlowBuffer(obj) || !!obj._isBuffer)
}

function isBuffer (obj) {
  return !!obj.constructor && typeof obj.constructor.isBuffer === 'function' && obj.constructor.isBuffer(obj)
}

// For Node v0.10 support. Remove this eventually.
function isSlowBuffer (obj) {
  return typeof obj.readFloatLE === 'function' && typeof obj.slice === 'function' && isBuffer(obj.slice(0, 0))
}


/***/ }),

/***/ "ZLW0":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
//
//
//
//
//

/* harmony default export */ __webpack_exports__["a"] = ({
  name: 'ElButtonGroup'
});

/***/ }),

/***/ "awzg":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator__ = __webpack_require__("Xxa5");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator__ = __webpack_require__("exGp");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator__);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__node_modules_element_ui_packages_button_src_button_group_vue__ = __webpack_require__("RvCN");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__config__ = __webpack_require__("iOPO");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__node_modules_element_ui_packages_button_src_button_vue__ = __webpack_require__("EMXe");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__node_modules_element_ui_packages_form_src_form_vue__ = __webpack_require__("xrpo");


//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//







/* harmony default export */ __webpack_exports__["a"] = ({
  components: {
    ElForm: __WEBPACK_IMPORTED_MODULE_5__node_modules_element_ui_packages_form_src_form_vue__["a" /* default */],
    ElButton: __WEBPACK_IMPORTED_MODULE_4__node_modules_element_ui_packages_button_src_button_vue__["a" /* default */],
    ElButtonGroup: __WEBPACK_IMPORTED_MODULE_2__node_modules_element_ui_packages_button_src_button_group_vue__["a" /* default */] },
  name: 'school',
  data: function data() {
    return {
      school_id: window.school_id,
      list: [],
      total: 0,
      search: '',
      page_size: 10,
      current_page: 1,
      loading: false,
      add_form: {
        name: '',
        register_username: "",
        register_password: '',
        visible: false

      },
      edit_form: {
        id: '',
        name: '',
        register_userid: '',
        register_username: '',
        register_password: '',
        visible: false,
        change_password: false
      },
      upload_dialog: {
        visible: false
      }
    };
  },


  watch: {
    current_page: function current_page() {
      this.fetch();
    }
  },

  methods: {
    change_page: function change_page(p) {
      console.log(p);
    },
    open_edit: function open_edit(data) {
      console.log(data);
      var change_password = this.edit_form.change_password;
      data.visible = true;
      this.edit_form = {
        visible: true,
        id: data.id,
        name: data.name,
        register_userid: data.register_userid,
        register_username: data.register_username,
        register_password: data.register_password,
        change_password: change_password
      };
    },
    fetch: function fetch() {
      var _this = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee() {
        var _limit, _page, search, that, response;

        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee$(_context) {
          while (1) {
            switch (_context.prev = _context.next) {
              case 0:
                _limit = _this.page_size, _page = _this.current_page, search = _this.search, that = _this;


                _this.loading = true;
                console.log(window.school, 'window.school');
                _context.next = 5;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].get('/api/school/');

              case 5:
                response = _context.sent;

                _this.list = response.data.objects;

                _this.loading = false;

              case 8:
              case "end":
                return _context.stop();
            }
          }
        }, _callee, _this);
      }))();
    },
    add: function add() {
      var _this2 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee2() {
        var add_form, response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee2$(_context2) {
          while (1) {
            switch (_context2.prev = _context2.next) {
              case 0:
                add_form = _this2.add_form;


                console.log(add_form, '----');

                _context2.next = 4;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].post('/api/school/', add_form);

              case 4:
                response = _context2.sent;

                _this2.add_form.visible = false;
                _this2.fetch();

              case 7:
              case "end":
                return _context2.stop();
            }
          }
        }, _callee2, _this2);
      }))();
    },
    remove: function remove(data) {
      var _this3 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee3() {
        var response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee3$(_context3) {
          while (1) {
            switch (_context3.prev = _context3.next) {
              case 0:
                _context3.prev = 0;
                _context3.next = 3;
                return _this3.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                  confirmButtonText: '确定',
                  cancelButtonText: '取消',
                  type: 'warning'
                });

              case 3:
                _context3.next = 5;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].delete('/api/school/' + data.id + '/');

              case 5:
                response = _context3.sent;


                _this3.$message({
                  type: 'success',
                  message: '删除成功!'
                });
                _this3.fetch();
                _context3.next = 13;
                break;

              case 10:
                _context3.prev = 10;
                _context3.t0 = _context3["catch"](0);

                _this3.$message({
                  type: 'info',
                  message: '已取消删除'
                });

              case 13:
              case "end":
                return _context3.stop();
            }
          }
        }, _callee3, _this3, [[0, 10]]);
      }))();
    },
    edit: function edit() {
      var _this4 = this;

      return __WEBPACK_IMPORTED_MODULE_1_babel_runtime_helpers_asyncToGenerator___default()( /*#__PURE__*/__WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.mark(function _callee4() {
        var edit_form, id, response;
        return __WEBPACK_IMPORTED_MODULE_0_babel_runtime_regenerator___default.a.wrap(function _callee4$(_context4) {
          while (1) {
            switch (_context4.prev = _context4.next) {
              case 0:
                edit_form = _this4.edit_form;

                console.log(edit_form);
                id = edit_form.id;


                _this4.$message({
                  type: 'success',
                  message: '修改信息成功!'
                });

                _context4.next = 6;
                return __WEBPACK_IMPORTED_MODULE_3__config__["a" /* default */].put('/api/school/' + id + '/', edit_form);

              case 6:
                response = _context4.sent;

                _this4.edit_form.visible = false;
                _this4.fetch();

              case 9:
              case "end":
                return _context4.stop();
            }
          }
        }, _callee4, _this4);
      }))();
    }
  },
  mounted: function mounted() {

    this.fetch();
  }
});

/***/ }),

/***/ "bwIi":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"teacher"},[_c('h5',[_vm._v("   总计"+_vm._s(_vm.total)+"条数据")]),_vm._v(" "),_c('el-form',{staticClass:"demo-form-inline",attrs:{"inline":true,"loading":_vm.loading}},[_c('el-form-item'),_vm._v(" "),_c('el-form-item',{attrs:{"label":"姓名"}},[_c('el-input',{attrs:{"placeholder":"输入姓名查询","size":"small"},model:{value:(_vm.search),callback:function ($$v) {_vm.search=$$v},expression:"search"}})],1),_vm._v(" "),_c('el-form-item',[_c('el-button-group',[_c('el-button',{attrs:{"type":"primary","size":"small"},on:{"click":_vm.fetch}},[_vm._v("查询")]),_vm._v(" "),_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.add_form.visible=true}}},[_vm._v("增加学校")])],1)],1)],1),_vm._v(" "),_c('el-table',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],staticStyle:{"width":"100%"},attrs:{"data":_vm.list,"border":"","size":"mini"}},[_c('el-table-column',{attrs:{"prop":"id","label":"id"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"office_name","label":"办公室名字"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"exam_name","label":"办公室负责考试"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"register_username","label":"注册用户名"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"register_password","label":"注册密码"}}),_vm._v(" "),_c('el-table-column',{attrs:{"label":"操作","width":"135"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [_c('el-button-group',[_c('el-button',{attrs:{"type":"danger","size":"small"},on:{"click":function($event){_vm.remove(scope.row)}}},[_vm._v("删除")]),_vm._v(" "),_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.open_edit(scope.row)}}},[_vm._v("编辑")])],1)]}}])})],1),_vm._v(" "),_c('el-dialog',{attrs:{"title":"增加办公室信息","visible":_vm.add_form.visible},on:{"update:visible":function($event){_vm.$set(_vm.add_form, "visible", $event)}}},[_c('el-form',{staticClass:"demo-form-inline",attrs:{"label-width":"100px"}},[_c('el-form-item',{attrs:{"label":"办公室名字"}},[_c('el-input',{attrs:{"placeholder":"办公室名字"},model:{value:(_vm.add_form.office_name),callback:function ($$v) {_vm.$set(_vm.add_form, "office_name", $$v)},expression:"add_form.office_name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"负责考试"}},[_c('el-input',{attrs:{"placeholder":"负责考试"},model:{value:(_vm.add_form.exam_name),callback:function ($$v) {_vm.$set(_vm.add_form, "exam_name", $$v)},expression:"add_form.exam_name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册用户名"}},[_c('el-input',{attrs:{"placeholder":"输入用户名"},model:{value:(_vm.add_form.register_username),callback:function ($$v) {_vm.$set(_vm.add_form, "register_username", $$v)},expression:"add_form.register_username"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册密码"}},[_c('el-input',{attrs:{"placeholder":"输入密码"},model:{value:(_vm.add_form.register_password),callback:function ($$v) {_vm.$set(_vm.add_form, "register_password", $$v)},expression:"add_form.register_password"}})],1)],1),_vm._v(" "),_c('span',{staticClass:"dialog-footer",attrs:{"slot":"footer"},slot:"footer"},[_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.add_form.visible=false}}},[_vm._v("取 消")]),_vm._v(" "),_c('el-button',{attrs:{"type":"primary","size":"small"},on:{"click":_vm.add}},[_vm._v("确 定")])],1)],1),_vm._v(" "),_c('el-dialog',{attrs:{"title":"编辑办公室信息","visible":_vm.edit_form.visible},on:{"update:visible":function($event){_vm.$set(_vm.edit_form, "visible", $event)}}},[_c('el-form',{staticClass:"demo-form-inline",attrs:{"label-width":"100px"}},[_c('el-form-item',{attrs:{"label":"办公室名字"}},[_c('el-input',{attrs:{"placeholder":"办公室名字"},model:{value:(_vm.edit_form.office_name),callback:function ($$v) {_vm.$set(_vm.edit_form, "office_name", $$v)},expression:"edit_form.office_name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"负责考试"}},[_c('el-input',{attrs:{"placeholder":"负责考试"},model:{value:(_vm.edit_form.exam_name),callback:function ($$v) {_vm.$set(_vm.edit_form, "exam_name", $$v)},expression:"edit_form.exam_name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册用户名"}},[_c('el-input',{attrs:{"placeholder":"输入用户名"},model:{value:(_vm.edit_form.register_username),callback:function ($$v) {_vm.$set(_vm.edit_form, "register_username", $$v)},expression:"edit_form.register_username"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"是否修改密码"}},[_c('el-switch',{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:(_vm.edit_form.change_password),callback:function ($$v) {_vm.$set(_vm.edit_form, "change_password", $$v)},expression:"edit_form.change_password"}})],1),_vm._v(" "),(_vm.edit_form.change_password)?_c('el-form-item',{attrs:{"label":"注册密码"}},[_c('el-input',{attrs:{"placeholder":"输入密码"},model:{value:(_vm.edit_form.register_password),callback:function ($$v) {_vm.$set(_vm.edit_form, "register_password", $$v)},expression:"edit_form.register_password"}})],1):_vm._e()],1),_vm._v(" "),_c('span',{staticClass:"dialog-footer",attrs:{"slot":"footer"},slot:"footer"},[_c('el-button',{on:{"click":function($event){_vm.edit_form.visible=false}}},[_vm._v("取 消")]),_vm._v(" "),_c('el-button',{attrs:{"type":"primary"},on:{"click":_vm.edit}},[_vm._v("确 定")])],1)],1),_vm._v(" "),_c('br'),_vm._v(" "),_c('el-pagination',{attrs:{"layout":"prev, pager, next","total":_vm.total,"current-page":_vm.current_page,"page-size":_vm.page_size},on:{"current-change":function (p){ return _vm.current_page=p; }}})],1)}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "i7gz":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var utils = __webpack_require__("zIVT");

/**
 * Transform the data for a request or a response
 *
 * @param {Object|String} data The data to be transformed
 * @param {Array} headers The headers for the request or response
 * @param {Array|Function} fns A single function or Array of functions
 * @returns {*} The resulting transformed data
 */
module.exports = function transformData(data, headers, fns) {
  /*eslint no-param-reassign:0*/
  utils.forEach(fns, function transform(fn) {
    data = fn(data, headers);
  });

  return data;
};


/***/ }),

/***/ "iOPO":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios__ = __webpack_require__("uj17");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_axios___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_axios__);


var request = __WEBPACK_IMPORTED_MODULE_0_axios___default.a.create({
  baseURL:''
})

/* harmony default export */ __webpack_exports__["a"] = (request);




/***/ }),

/***/ "jiPp":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_school_vue__ = __webpack_require__("awzg");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_7f660d26_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_school_vue__ = __webpack_require__("v/XQ");
function injectStyle (ssrContext) {
  __webpack_require__("AZqh")
}
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = injectStyle
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_school_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_7f660d26_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_school_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "lcrx":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["a"] = ({
  name: 'ElForm',

  componentName: 'ElForm',

  provide: function provide() {
    return {
      elForm: this
    };
  },


  props: {
    model: Object,
    rules: Object,
    labelPosition: String,
    labelWidth: String,
    labelSuffix: {
      type: String,
      default: ''
    },
    inline: Boolean,
    inlineMessage: Boolean,
    statusIcon: Boolean,
    showMessage: {
      type: Boolean,
      default: true
    },
    size: String
  },
  watch: {
    rules: function rules() {
      this.validate();
    }
  },
  data: function data() {
    return {
      fields: []
    };
  },
  created: function created() {
    var _this = this;

    this.$on('el.form.addField', function (field) {
      if (field) {
        _this.fields.push(field);
      }
    });
    /* istanbul ignore next */
    this.$on('el.form.removeField', function (field) {
      if (field.prop) {
        _this.fields.splice(_this.fields.indexOf(field), 1);
      }
    });
  },

  methods: {
    resetFields: function resetFields() {
      if (!this.model) {
        "production" !== 'production' && console.warn('[Element Warn][Form]model is required for resetFields to work.');
        return;
      }
      this.fields.forEach(function (field) {
        field.resetField();
      });
    },
    clearValidate: function clearValidate() {
      this.fields.forEach(function (field) {
        field.clearValidate();
      });
    },
    validate: function validate(callback) {
      var _this2 = this;

      if (!this.model) {
        console.warn('[Element Warn][Form]model is required for validate to work!');
        return;
      }

      var promise = void 0;
      // if no callback, return promise
      if (typeof callback !== 'function' && window.Promise) {
        promise = new window.Promise(function (resolve, reject) {
          callback = function callback(valid) {
            valid ? resolve(valid) : reject(valid);
          };
        });
      }

      var valid = true;
      var count = 0;
      // 如果需要验证的fields为空，调用验证时立刻返回callback
      if (this.fields.length === 0 && callback) {
        callback(true);
      }
      this.fields.forEach(function (field, index) {
        field.validate('', function (errors) {
          if (errors) {
            valid = false;
          }
          if (typeof callback === 'function' && ++count === _this2.fields.length) {
            callback(valid);
          }
        });
      });

      if (promise) {
        return promise;
      }
    },
    validateField: function validateField(prop, cb) {
      var field = this.fields.filter(function (field) {
        return field.prop === prop;
      })[0];
      if (!field) {
        throw new Error('must call validateField with valid prop string!');
      }

      field.validate('', cb);
    }
  }
});

/***/ }),

/***/ "lv6U":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "oYwm":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('form',{staticClass:"el-form",class:[
  _vm.labelPosition ? 'el-form--label-' + _vm.labelPosition : '',
  { 'el-form--inline': _vm.inline }
]},[_vm._t("default")],2)}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "oaLO":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0_vue__ = __webpack_require__("7+uW");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1_vue_router__ = __webpack_require__("/ocq");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__components_office_vue__ = __webpack_require__("A9Yy");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__components_school_vue__ = __webpack_require__("jiPp");






__WEBPACK_IMPORTED_MODULE_0_vue__["default"].use(__WEBPACK_IMPORTED_MODULE_1_vue_router__["a" /* default */])

/* harmony default export */ __webpack_exports__["a"] = (new __WEBPACK_IMPORTED_MODULE_1_vue_router__["a" /* default */]({
  routes: [
    {
      path: '/',
      name: 'office',
      component: __WEBPACK_IMPORTED_MODULE_2__components_office_vue__["a" /* default */]
    },
    {
      path: '/office',
      name: 'office',
      component: __WEBPACK_IMPORTED_MODULE_2__components_office_vue__["a" /* default */]
    },
    {
      path: '/school',
      name: 'school',
      component: __WEBPACK_IMPORTED_MODULE_3__components_school_vue__["a" /* default */]
    },

  ]
}));


/***/ }),

/***/ "obgR":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * Update an Error with the specified config, error code, and response.
 *
 * @param {Error} error The error to update.
 * @param {Object} config The config.
 * @param {string} [code] The error code (for example, 'ECONNABORTED').
 * @param {Object} [request] The request.
 * @param {Object} [response] The response.
 * @returns {Error} The error.
 */
module.exports = function enhanceError(error, config, code, request, response) {
  error.config = config;
  if (code) {
    error.code = code;
  }
  error.request = request;
  error.response = response;
  return error;
};


/***/ }),

/***/ "q8By":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//

/* harmony default export */ __webpack_exports__["a"] = ({
    name: 'app',
    data: function data() {
        var name = this.$route.path;
        return {
            name: name,

            user: window.user
        };
    },

    methods: {
        route: function route(name) {
            this.$router.push(name);
        }
    },
    mounted: function mounted() {}
});

/***/ }),

/***/ "tvR6":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "u6N1":
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ "uj17":
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__("HXpE");

/***/ }),

/***/ "v/XQ":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"teacher"},[_c('h5',[_vm._v("   总计"+_vm._s(_vm.total)+"条数据")]),_vm._v(" "),_c('el-form',{staticClass:"demo-form-inline",attrs:{"inline":true,"loading":_vm.loading}},[_c('el-form-item'),_vm._v(" "),_c('el-form-item',{attrs:{"label":"姓名"}},[_c('el-input',{attrs:{"placeholder":"输入姓名查询","size":"small"},model:{value:(_vm.search),callback:function ($$v) {_vm.search=$$v},expression:"search"}})],1),_vm._v(" "),_c('el-form-item',[_c('el-button-group',[_c('el-button',{attrs:{"type":"primary","size":"small"},on:{"click":_vm.fetch}},[_vm._v("查询")]),_vm._v(" "),_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.add_form.visible=true}}},[_vm._v("增加学校")])],1)],1)],1),_vm._v(" "),_c('el-table',{directives:[{name:"loading",rawName:"v-loading",value:(_vm.loading),expression:"loading"}],staticStyle:{"width":"100%"},attrs:{"data":_vm.list,"border":"","size":"mini"}},[_c('el-table-column',{attrs:{"prop":"id","label":"id"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"name","label":"名字"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"register_username","label":"注册用户名"}}),_vm._v(" "),_c('el-table-column',{attrs:{"prop":"register_password","label":"注册密码"}}),_vm._v(" "),_c('el-table-column',{attrs:{"label":"操作","width":"135"},scopedSlots:_vm._u([{key:"default",fn:function(scope){return [_c('el-button-group',[_c('el-button',{attrs:{"type":"danger","size":"small"},on:{"click":function($event){_vm.remove(scope.row)}}},[_vm._v("删除")]),_vm._v(" "),_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.open_edit(scope.row)}}},[_vm._v("编辑")])],1)]}}])})],1),_vm._v(" "),_c('el-dialog',{attrs:{"title":"增加老师信息","visible":_vm.add_form.visible},on:{"update:visible":function($event){_vm.$set(_vm.add_form, "visible", $event)}}},[_c('el-form',{staticClass:"demo-form-inline",attrs:{"label-width":"100px"}},[_c('el-form-item',{attrs:{"label":"姓名"}},[_c('el-input',{attrs:{"placeholder":"输入姓名"},model:{value:(_vm.add_form.name),callback:function ($$v) {_vm.$set(_vm.add_form, "name", $$v)},expression:"add_form.name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册用户名"}},[_c('el-input',{attrs:{"placeholder":"输入用户名"},model:{value:(_vm.add_form.register_username),callback:function ($$v) {_vm.$set(_vm.add_form, "register_username", $$v)},expression:"add_form.register_username"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册密码"}},[_c('el-input',{attrs:{"placeholder":"输入密码"},model:{value:(_vm.add_form.register_password),callback:function ($$v) {_vm.$set(_vm.add_form, "register_password", $$v)},expression:"add_form.register_password"}})],1)],1),_vm._v(" "),_c('span',{staticClass:"dialog-footer",attrs:{"slot":"footer"},slot:"footer"},[_c('el-button',{attrs:{"size":"small"},on:{"click":function($event){_vm.add_form.visible=false}}},[_vm._v("取 消")]),_vm._v(" "),_c('el-button',{attrs:{"type":"primary","size":"small"},on:{"click":_vm.add}},[_vm._v("确 定")])],1)],1),_vm._v(" "),_c('el-dialog',{attrs:{"title":"编辑老师信息","visible":_vm.edit_form.visible},on:{"update:visible":function($event){_vm.$set(_vm.edit_form, "visible", $event)}}},[_c('el-form',{staticClass:"demo-form-inline",attrs:{"label-width":"100px"}},[_c('el-form-item',{attrs:{"label":"姓名"}},[_c('el-input',{attrs:{"placeholder":"输入姓名"},model:{value:(_vm.edit_form.name),callback:function ($$v) {_vm.$set(_vm.edit_form, "name", $$v)},expression:"edit_form.name"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"注册用户名"}},[_c('el-input',{attrs:{"placeholder":"输入用户名"},model:{value:(_vm.edit_form.register_username),callback:function ($$v) {_vm.$set(_vm.edit_form, "register_username", $$v)},expression:"edit_form.register_username"}})],1),_vm._v(" "),_c('el-form-item',{attrs:{"label":"是否修改密码"}},[_c('el-switch',{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:(_vm.edit_form.change_password),callback:function ($$v) {_vm.$set(_vm.edit_form, "change_password", $$v)},expression:"edit_form.change_password"}})],1),_vm._v(" "),(_vm.edit_form.change_password)?_c('el-form-item',{attrs:{"label":"注册密码"}},[_c('el-input',{attrs:{"placeholder":"输入密码"},model:{value:(_vm.edit_form.register_password),callback:function ($$v) {_vm.$set(_vm.edit_form, "register_password", $$v)},expression:"edit_form.register_password"}})],1):_vm._e()],1),_vm._v(" "),_c('span',{staticClass:"dialog-footer",attrs:{"slot":"footer"},slot:"footer"},[_c('el-button',{on:{"click":function($event){_vm.edit_form.visible=false}}},[_vm._v("取 消")]),_vm._v(" "),_c('el-button',{attrs:{"type":"primary"},on:{"click":_vm.edit}},[_vm._v("确 定")])],1)],1),_vm._v(" "),_c('br'),_vm._v(" "),_c('el-pagination',{attrs:{"layout":"prev, pager, next","total":_vm.total,"current-page":_vm.current_page,"page-size":_vm.page_size},on:{"current-change":function (p){ return _vm.current_page=p; }}})],1)}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ }),

/***/ "wZW9":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var createError = __webpack_require__("0l+G");

/**
 * Resolve or reject a Promise based on response status.
 *
 * @param {Function} resolve A function that resolves the promise.
 * @param {Function} reject A function that rejects the promise.
 * @param {object} response The response.
 */
module.exports = function settle(resolve, reject, response) {
  var validateStatus = response.config.validateStatus;
  // Note: status is not exposed by XDomainRequest
  if (!response.status || !validateStatus || validateStatus(response.status)) {
    resolve(response);
  } else {
    reject(createError(
      'Request failed with status code ' + response.status,
      response.config,
      null,
      response.request,
      response
    ));
  }
};


/***/ }),

/***/ "xrpo":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_form_vue__ = __webpack_require__("lcrx");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_70576002_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_form_vue__ = __webpack_require__("oYwm");
var normalizeComponent = __webpack_require__("VU/8")
/* script */

/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = null
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_vue_loader_lib_selector_type_script_index_0_form_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__vue_loader_lib_template_compiler_index_id_data_v_70576002_hasScoped_false_transformToRequire_video_src_source_src_img_src_image_xlink_href_buble_transforms_vue_loader_lib_selector_type_template_index_0_form_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["a"] = (Component.exports);


/***/ }),

/***/ "zIVT":
/***/ (function(module, exports, __webpack_require__) {

"use strict";


var bind = __webpack_require__("4nb4");
var isBuffer = __webpack_require__("ZH5x");

/*global toString:true*/

// utils is a library of generic helper functions non-specific to axios

var toString = Object.prototype.toString;

/**
 * Determine if a value is an Array
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an Array, otherwise false
 */
function isArray(val) {
  return toString.call(val) === '[object Array]';
}

/**
 * Determine if a value is an ArrayBuffer
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an ArrayBuffer, otherwise false
 */
function isArrayBuffer(val) {
  return toString.call(val) === '[object ArrayBuffer]';
}

/**
 * Determine if a value is a FormData
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an FormData, otherwise false
 */
function isFormData(val) {
  return (typeof FormData !== 'undefined') && (val instanceof FormData);
}

/**
 * Determine if a value is a view on an ArrayBuffer
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a view on an ArrayBuffer, otherwise false
 */
function isArrayBufferView(val) {
  var result;
  if ((typeof ArrayBuffer !== 'undefined') && (ArrayBuffer.isView)) {
    result = ArrayBuffer.isView(val);
  } else {
    result = (val) && (val.buffer) && (val.buffer instanceof ArrayBuffer);
  }
  return result;
}

/**
 * Determine if a value is a String
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a String, otherwise false
 */
function isString(val) {
  return typeof val === 'string';
}

/**
 * Determine if a value is a Number
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Number, otherwise false
 */
function isNumber(val) {
  return typeof val === 'number';
}

/**
 * Determine if a value is undefined
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if the value is undefined, otherwise false
 */
function isUndefined(val) {
  return typeof val === 'undefined';
}

/**
 * Determine if a value is an Object
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is an Object, otherwise false
 */
function isObject(val) {
  return val !== null && typeof val === 'object';
}

/**
 * Determine if a value is a Date
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Date, otherwise false
 */
function isDate(val) {
  return toString.call(val) === '[object Date]';
}

/**
 * Determine if a value is a File
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a File, otherwise false
 */
function isFile(val) {
  return toString.call(val) === '[object File]';
}

/**
 * Determine if a value is a Blob
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Blob, otherwise false
 */
function isBlob(val) {
  return toString.call(val) === '[object Blob]';
}

/**
 * Determine if a value is a Function
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Function, otherwise false
 */
function isFunction(val) {
  return toString.call(val) === '[object Function]';
}

/**
 * Determine if a value is a Stream
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a Stream, otherwise false
 */
function isStream(val) {
  return isObject(val) && isFunction(val.pipe);
}

/**
 * Determine if a value is a URLSearchParams object
 *
 * @param {Object} val The value to test
 * @returns {boolean} True if value is a URLSearchParams object, otherwise false
 */
function isURLSearchParams(val) {
  return typeof URLSearchParams !== 'undefined' && val instanceof URLSearchParams;
}

/**
 * Trim excess whitespace off the beginning and end of a string
 *
 * @param {String} str The String to trim
 * @returns {String} The String freed of excess whitespace
 */
function trim(str) {
  return str.replace(/^\s*/, '').replace(/\s*$/, '');
}

/**
 * Determine if we're running in a standard browser environment
 *
 * This allows axios to run in a web worker, and react-native.
 * Both environments support XMLHttpRequest, but not fully standard globals.
 *
 * web workers:
 *  typeof window -> undefined
 *  typeof document -> undefined
 *
 * react-native:
 *  navigator.product -> 'ReactNative'
 */
function isStandardBrowserEnv() {
  if (typeof navigator !== 'undefined' && navigator.product === 'ReactNative') {
    return false;
  }
  return (
    typeof window !== 'undefined' &&
    typeof document !== 'undefined'
  );
}

/**
 * Iterate over an Array or an Object invoking a function for each item.
 *
 * If `obj` is an Array callback will be called passing
 * the value, index, and complete array for each item.
 *
 * If 'obj' is an Object callback will be called passing
 * the value, key, and complete object for each property.
 *
 * @param {Object|Array} obj The object to iterate
 * @param {Function} fn The callback to invoke for each item
 */
function forEach(obj, fn) {
  // Don't bother if no value provided
  if (obj === null || typeof obj === 'undefined') {
    return;
  }

  // Force an array if not already something iterable
  if (typeof obj !== 'object') {
    /*eslint no-param-reassign:0*/
    obj = [obj];
  }

  if (isArray(obj)) {
    // Iterate over array values
    for (var i = 0, l = obj.length; i < l; i++) {
      fn.call(null, obj[i], i, obj);
    }
  } else {
    // Iterate over object keys
    for (var key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        fn.call(null, obj[key], key, obj);
      }
    }
  }
}

/**
 * Accepts varargs expecting each argument to be an object, then
 * immutably merges the properties of each object and returns result.
 *
 * When multiple objects contain the same key the later object in
 * the arguments list will take precedence.
 *
 * Example:
 *
 * ```js
 * var result = merge({foo: 123}, {foo: 456});
 * console.log(result.foo); // outputs 456
 * ```
 *
 * @param {Object} obj1 Object to merge
 * @returns {Object} Result of all merge properties
 */
function merge(/* obj1, obj2, obj3, ... */) {
  var result = {};
  function assignValue(val, key) {
    if (typeof result[key] === 'object' && typeof val === 'object') {
      result[key] = merge(result[key], val);
    } else {
      result[key] = val;
    }
  }

  for (var i = 0, l = arguments.length; i < l; i++) {
    forEach(arguments[i], assignValue);
  }
  return result;
}

/**
 * Extends object a by mutably adding to it the properties of object b.
 *
 * @param {Object} a The object to be extended
 * @param {Object} b The object to copy properties from
 * @param {Object} thisArg The object to bind function to
 * @return {Object} The resulting value of object a
 */
function extend(a, b, thisArg) {
  forEach(b, function assignValue(val, key) {
    if (thisArg && typeof val === 'function') {
      a[key] = bind(val, thisArg);
    } else {
      a[key] = val;
    }
  });
  return a;
}

module.exports = {
  isArray: isArray,
  isArrayBuffer: isArrayBuffer,
  isBuffer: isBuffer,
  isFormData: isFormData,
  isArrayBufferView: isArrayBufferView,
  isString: isString,
  isNumber: isNumber,
  isObject: isObject,
  isUndefined: isUndefined,
  isDate: isDate,
  isFile: isFile,
  isBlob: isBlob,
  isFunction: isFunction,
  isStream: isStream,
  isURLSearchParams: isURLSearchParams,
  isStandardBrowserEnv: isStandardBrowserEnv,
  forEach: forEach,
  merge: merge,
  extend: extend,
  trim: trim
};


/***/ })

},["5ovs"]);
//# sourceMappingURL=center.js.map