<template>
  <div class="teacher">

    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{path:'/teacher_list?id='+$route.query.id}">学校管理({{detail.name}})</el-breadcrumb-item>
      <el-breadcrumb-item>批量导入</el-breadcrumb-item>
    </el-breadcrumb>

    <br/>
    <el-form :inline="true" class="demo-form-inline" >



      <el-form-item

      >
        <el-upload
          class="upload-demo"
          ref="upload"
          action="/upload/"
          name="file"
          :on-success="success"

          multiple
         >
          <el-button slot="trigger" size="mini" type="primary">上传身份证</el-button>


        </el-upload>
      </el-form-item>
      <el-form-item >
          <el-button size="mini" type="primary"  @click="  download_template ">下载模板</el-button>
      </el-form-item>
      <el-form-item>
        <input type="file" @change="onchange" value="上传老师表格"/>
      </el-form-item>

      <el-form-item>
        <el-button type="danger" size="small" @click="save">
          提交
        </el-button>
      </el-form-item>
    </el-form>

      <el-row :gutter="20">
        <el-col></el-col>
      </el-row>
    <el-table
        :data="list"
        style="width: 100%"
        border
        size="mini"
        v-loading="loading"
      >


      <el-table-column  label="序号">
        <template scope="scope">
          {{scope.$index}}
        </template>
      </el-table-column>
        <el-table-column prop="name" label="教师姓名"></el-table-column>
   


        <el-table-column prop="idcard"  label="身份证"></el-table-column>
        <el-table-column prop="bankcard"  label="银行卡号"></el-table-column>
        <el-table-column prop="bankinfo"  label="银行信息"></el-table-column>
        <el-table-column prop="phone"  label="电话号码"></el-table-column>

      </el-table>







  </div>
</template>

<script>

  import ElButtonGroup from "../../node_modules/element-ui/packages/button/src/button-group.vue";
  import request from './config'
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
  import ElCol from "element-ui/packages/col/src/col";
  import moment from 'moment'
  import req from 'axios'
  import ElFormItem from "../../node_modules/element-ui/packages/form/src/form-item.vue";
  import download from './excel-download.vue'
export default {
  components: {
    ElFormItem,
    ElCol,
    ElButton,
    ElButtonGroup,
    download
  },

  name: 'muti-teacher',
  data () {
    return {
      detail:{},
      school_id:window.school_id,
      list:[
      //  {
      //    phone: "1321231",
      //    idcard: "899333622",
      //    name: "六六",
      //    bankcard: "321多撒多打",
      //    bankinfo: "3的撒大声多阿萨德"
      //  },
      //  {
      //    phone: "11111",
      //    idcard: "3434643",
      //    name: "七七",
      //    bankcard: "31313",
      //    bankinfo: "3奥术大师爱迪生爱迪生"
      //  },

      ],
      loading:false




    }
  },

  watch:{
      current_page(){
          this.fetch()
      }
  },

  methods:{
    download_template(){
      location.href = '/teacherexport?school_id='+this.$route.query.id
    },

    onchange(f){
      var that = this
      var file = f.target.files[0]

      var name = file.name;
      var reader = new FileReader();
      reader.onload = function (e) {
        console.log('hello world')
        var data = e.target.result;
        console.log(data)
        var wb = XLSX.read(data, { type: "binary" });

        var list =  XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
        list = list.map(function(obj){
          obj.name = obj['姓名'] ? obj['姓名'].trim() : ''
          obj.idcard = obj['身份证号'] ? obj['身份证号'].trim() : ''
          obj.phone = obj['电话'] ? obj['电话'].trim() : ''
          obj.bankcard = obj['银行卡号'] ? obj['银行卡号'].trim() : ''
          obj.bankinfo = obj['银行信息'] ? obj['银行信息'].trim() : ''
          return obj
        })
        that.list = list
        
      };
      reader.readAsBinaryString(file);
    },

    async save(){
      try{
        await this.$confirm('请认真检查数据是否正确', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
        var list = this.list
        var id = this.$route.query.id
        var req = await request.post('/api2/teacher/',{
          list:list,
          school_id:id
        })
        this.list = []
        this.$message({
          type: 'success',
          message: `创建了${req.data.create}条数据，有${list.length-req.data.create*1}条数据重复`
        });

      }catch (e){
        this.$message({
          type: 'info',
          message: '已取消提交'
        });
      }

    },
    success(res){
      var obj = res.cards[0]
      this.list = this.list.concat({
        name:obj.name,
        idcard:obj.id_card_number,
        phone:'',
        bankcard:'',
        bankinfo:''
      })

    },
    async fetch_school(){
      var id = this.$route.query.id
      var response = await request.get('/api/school/'+id+'/')
      this.detail = response.data
      console.log(response.data)
    },

    async fetch_teacher(){
          this.loading = true 
          var response = await request.get('/api/teacher/?school_id='+this.$route.query.id,{
            params:{
              no_page:1
            }
          })
          this.list = response.data.objects
          this.list = this.list.map(function (item) {
            item.create_time = moment(item.create_time).format('YYYY-MM-DD')
            item.name = item.name.trim()
            item.bankinfo = item.bankinfo.trim()
            item.bankinfo = item.bankinfo.trim()
            item.phone = item.phone.trim()
            item.idcard = item.idcard.trim()
            return item
          })
       
        this.loading = false

    }

  },
  mounted(){
    this.fetch_school()
    this.fetch_teacher()
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
