<template>
  <div class="teacher">

    <!--<el-breadcrumb separator="/">-->
      <!--<el-breadcrumb-item :to="{ path: '/school_list' }">首页</el-breadcrumb-item>-->
      <!--<el-breadcrumb-item :to="{path:'/teacher_list?id='+$route.query.id}">学校管理({{detail.name}})</el-breadcrumb-item>-->
      <!--<el-breadcrumb-item>批量导入</el-breadcrumb-item>-->
    <!--</el-breadcrumb>-->
    <h3>{{exam_item.desc}}</h3>

    <el-form :inline="true" class="demo-form-inline" >

      <el-form-item
      >
      </el-form-item>
      <el-form-item >
          <el-button size="mini" type="primary"  @click="  download_template ">下载模板</el-button>
      </el-form-item>
      <el-form-item>
        <input type="file" @change="onchange" value="上传"/>
      </el-form-item>

      <el-form-item>
        <el-button type="danger" size="small" @click="save">
          提交
        </el-button>
      </el-form-item>
    </el-form>

      <el-row :gutter="30">
         <h4>
            原始数据
          </h4>
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
        <el-table-column prop="name" label="学校名"></el-table-column>
        <el-table-column prop="total"  label="监考费"></el-table-column>
                <el-table-column prop="status"  label="状态"></el-table-column>
      </el-table>


      </el-row>












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
      error_list:[],
      list:[

      ],

      loading:false,
      exam_item:{

      }




    }
  },

  watch:{
      current_page(){
          this.fetch()
      }
  },

  methods:{
    download_template(){
      location.href = '/officetemplate?id='+this.$route.query.id
    },

    onchange(f){
      var that = this
      var file = f.target.files[0]

      var name = file.name;
      var reader = new FileReader();
      reader.onload = function (e) {

        var data = e.target.result;

        var wb = XLSX.read(data, { type: "binary" });

        var list =  XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
        list = list.map(function(obj){
          obj.name = obj['学校名'] || ''
          obj.total = obj['监考费'] || ''
          obj.status = '等待上传'
          return obj
        })
        console.log(list,'change-list')
        that.list = list

      };
      reader.readAsBinaryString(file);
    },

     async fetch_exam(){
         var id = this.$route.query.id

        var response = await request.get('/api/exam/'+id +'/')

        this.exam_item = response.data


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
        var req = await request.post('/api2/schoolexam/',{
          list:list,
          exam_id:id
        })
        console.log(req.data)
        this.list = req.data.list
         this.$message({
          type: 'success',
          message: '批量上传成功'
        });
        // this.$message({
        //   type: 'success',
        //   message: `创建了${req.data.create}条数据，有${list.length-req.data.create*1}条数据重复`
        // });

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
    async fetch(){
      let id  = this.$route.query.id
      let res = await request.get('/api/schoolexam/?page_size=2000&exam_id='+id)
      console.log(res.data,'-----')
      let list = res.data.objects
      list = list.map((obj)=>{
        obj.name = obj.school_name
        obj.status = 'ready'
        return obj
      })
      this.list =list
    },



  },
  mounted(){
    this.fetch()
    this.fetch_exam()
  }


}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
