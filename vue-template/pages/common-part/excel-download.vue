<template>
  <!-- <el-button class="export-btn el-button--export" @click="downloadExcel">导出</el-button> -->
  <div>
    <el-button  @click="downloadExcel" type="primary" size="small">{{title}}</el-button>
  </div>

</template>
<script>


  export default {


    props: {
      title: String,
      data:Array
    },
    methods: {

      downloadExcel() {
        var data = this.data
        console.log('data----',data)
        var base = this.data[0]
        if(data.length == 0)
        data.push({
            "姓名": "",
            "身份证号": "",
            "电话": "",
            "银行卡号": "",
            "银行信息": ""
        })
      
        const wopts = { bookType: 'xlsx', bookSST: true, type: 'binary' },
          wb = { SheetNames: ['Sheet1'], Sheets: {}, Props: {} };
        var data = XLSX.utils.json_to_sheet(data);
        wb.Sheets['Sheet1'] = data;
        this.saveAs(new Blob([this.s2ab(XLSX.write(wb, wopts))], { type: "application/octet-stream"}), `${this.title}.${(wopts.bookType == "biff2" ? "xls" : wopts.bookType)}`);
      },
      saveAs(obj, fileName) {
        var tmpa = document.createElement("a");
        tmpa.download = fileName || "下载";
        tmpa.href = URL.createObjectURL(obj); //绑定a标签
        tmpa.click();
        setTimeout(function () {
          URL.revokeObjectURL(obj);
        }, 100);
      },

      s2ab(s) {
        if (typeof ArrayBuffer !== 'undefined') {
          var buf = new ArrayBuffer(s.length);
          var view = new Uint8Array(buf);
          for (var i = 0; i != s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
          return buf;
        } else {
          var buf = new Array(s.length);
          for (var i = 0; i != s.length; ++i) buf[i] = s.charCodeAt(i) & 0xFF;
          return buf;
        }
      },

    }


    }
</script>
