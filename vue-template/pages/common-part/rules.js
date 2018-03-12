var idcard =  /^\d{6}(18|19|20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|[xX])$/
var bankcard =  /^\d{6}(18|19|20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|[xX])$/
export default {
  no_empty: [
    { required: true, message: '该字段是必填项' ,trigger:'change'},
  ],
  phone: [
    { required:true,pattern:/^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$/,message:'请输入正确格式的手机号码',trigger:'change'}
  ],
  idcard:[
    {required:true,pattern:idcard,message:'请输入18位身份证号',trigger:'change'}
  ],
  bankcard :[
    {required:true,pattern:/^\d+$/,message:'请输入正确的银行卡号',trigger:'change'}
  ]
}


//   phone:/^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}/,
//   idcard:/^\d{15}|\d{18}$/
