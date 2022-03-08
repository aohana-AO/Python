import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

import streamlit.components.v1 as stc
st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "MObile phone")

    
)

def page1():
   st.write("Here is page 1.")
   stc.html(
    """
    <meta charset="utf-8"/>
   <meta name="author" content="Mntn&reg; c/o Benjamin Lips"/>

   <style type="text/css">
   <!--
   ::selection{background:aquamarine;color:white;}
   ::-webkit-selection{background:aquamarine;color:white;}
   ::-moz-selection{background:aquamarine;color:white;}
   body{background:rgb(0, 0, 0);color:rgb(255, 255, 255);}
   *{cursor:default;font-family:'Vollkorn',monospace;line-height:4vw;font-size:3vw;padding:0;outline:0;margin:0;}
   #t{position:absolute;bottom:30%;left:50%;width: 1200px; margin-left:-650px;visibility:hidden;white-space:pre-wrap;}
   a{color:mediumslateblue;text-decoration:none;border-bottom:1px solid aquamarine;}
   code{background:rgb(213, 39, 0);}
   .g{color:rgb(250, 11, 11);}
   .p{color:rgb(116, 0, 19);}
   ins,del{text-decoration:none;}
   s{display:none;}
   kbd{font-family:inherit;}
   
   .t-caret{font-size:inherit;color:rgb(255, 255, 255);}
   @media(max-width:800px){#t{width:400px;margin-left:-200px;}}
   -->
   </style>
   <script src="https://cdn.jsdelivr.net/npm/jquery@3.3.1/dist/jquery.min.js"></script> <!-- 3.3.1 -->
   <script src="https://cdn.jsdelivr.net/gh/mntn-dev/t.js/t.min.js"></script> 
   <script type="text/javascript">
   //<![CDATA[
   $(function(){
   $('#t').t({
      
   delay:2,                   // start delay in seconds [default:0]
      
   speed:50,                  // typing speed (ms) [default:50]
   speed_vary:false,          // 'human like' speed variation [default:false]
      
   beep:true,                 // beep while typing (Web Audio API) [default:false]
      
   mistype:3,                 // mistype rate: 1:N per char [default:false]
   locale:'en',               // keyboard layout (to fit mistype); supported: 'en' (english) or 'de' (german) [default:'en']
      
   caret:'\u2589',            // caret content; can be html too [default:true (\u258e)]
   blink:true,                // blink-interval in ms; if TRUE, speed*3  [default:true]
   blink_perm:false,          // permanent blinking? if FALSE, caret blinks only on delay/pause/finish [default:false]
   repeat:0,                  // repeat typing: if TRUE, infinite or N times [default:0]
   tag:'span',                // wrapper tag (.t-container, .t-caret) [default:'span']
   pause_on_click:true,       // pauses/continues typing on click/tap (elm) [default:false]
   pause_on_tab_switch:true,  // pauses typing if window is inactive (Page Visibility API) [default:false]
      
   // init callback (ready-to-type)
   init:function(elm){},        
   // typing callback
   typing:function(elm,chr_or_elm,left,total){},
   // finished callback
   fin:function(elm){}          
      
   });
      
   });
   //]]>
   </script>
   </head>
   <body>
   <div id="t"><strong>SCP Foundation</strong> 

   <kbd>Secure</kbd>
   <kbd>Contain</kbd>
   <kbd>Protect</kbd>

   <em>SCP Foundation<del><ins>1</ins></del>SCP-ZAIDANN-NIHONNSIBU</em>
   International Translation Archive

   <img src="sozai2/icon_101630.svg" width="60" height="50" alt="日本財団支部">【SCP財団日本支部】

   <span class="g">【</span><ins>1.5</ins>アクセス制限：プロトコルB<span class="g">】</span><em><del>level2<ins>1</ins></del>level4</em>,  
   <kbd>本ファイルはSCP財団により収容されています。
   SCP-040-jp担当職員以外の<strong>アクセスは許可されていません。</strong>
   詳細なアクセス制限・内容についてはアクセス後ファイルに表示されています。
   【注意】誤アクセスを防ぐため、アクセス後も再度警告されます </kbd>
   SCP,Clearancelevel2,→4,<ins>1</ins>
   <span class="g">〔user〕</span>Access restrictions (Please login)<ins>.5</ins>
   ID:<kbd>scp-jp-huo8u99</kbd>
   Password:<kbd>774hwv8hvhw9hus_8u_f89sh8s8hfs</kbd>
   login : succese
   〔scp-jp-huo8u99〕level4,SCP-040-jp担当職員<ins>.5</ins>
   Access : success  アクセス完了
   
   <a target="_blank" href="index-neko1.html">SCP_Foundation 本部-全収容リスト</a>.
   <ins>5</ins>(Open file)<br/><span style="border-bottom:1px dashed rgb(126, 0, 0);">'ファイルに移動'→('<a target="_blank" href="neko1.html">pls clickfile</a>')</span> 
   </div>
   <br/>
   </body>
   """,width=500)
   st.title("すとりーむりっと練習")
   """
   # サンプル
   8 x 8の表データを表示する
   """
   
   dataframe = pd.DataFrame(
      np.random.randn(8, 8),
      columns=('col %d' % i for i in range(8)))
   st.table(dataframe)

   chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns=['a', 'b', 'c'])

   st.line_chart(chart_data)


   stc.html("""
         <meta name="viewport" content="width=device-width, initial-scale=1">
         <style>
         * {
         box-sizing: border-box;
         }

         body {
         margin: 0;
         font-family: Arial;
         }

         /* The grid: Four equal columns that floats next to each other */
         .column {
         float: left;
         width: 25%;
         padding: 10px;
         }

         /* Style the images inside the grid */
         .column img {
         opacity: 0.8; 
         cursor: pointer; 
         }

         .column img:hover {
         opacity: 1;
         }

         /* Clear floats after the columns */
         .row:after {
         content: "";
         display: table;
         clear: both;
         }

         /* The expanding image container */
         .container {
         position: relative;
         display: none;
         }

         /* Expanding image text */
         #imgtext {
         position: absolute;
         bottom: 15px;
         left: 15px;
         color: white;
         font-size: 20px;
         }

         /* Closable button inside the expanded image */
         .closebtn {
         position: absolute;
         top: 10px;
         right: 15px;
         color: white;
         font-size: 35px;
         cursor: pointer;
         }
         </style>
         </head>
         <body>

         <div style="text-align:center">
         <h2>Tabbed Image Gallery</h2>
         <p>Click on the images below:</p>
         </div>

         <!-- The four columns -->
         <div class="row">
         <div class="column">
               <img src="https://www.w3schools.com/howto/img_nature.jpg" alt="Nature" style="width:100%" onclick="myFunction(this);">
         </div>
         <div class="column">
               <img src="https://www.w3schools.com/howto/img_snow.jpg" alt="Snow" style="width:100%" onclick="myFunction(this);">
         </div>
         <div class="column">
               <img src="https://www.w3schools.com/howto/img_mountains.jpg" alt="Mountains" style="width:100%" onclick="myFunction(this);">
         </div>
         <div class="column">
               <img src="https://www.w3schools.com/howto/img_lights.jpg" alt="Lights" style="width:100%" onclick="myFunction(this);">
         </div>
         </div>

         <div class="container">
         <span onclick="this.parentElement.style.display='none'" class="closebtn">&times;</span>
         <img id="expandedImg" style="width:100%">
         <div id="imgtext"></div>
         </div>

         <script>
         function myFunction(imgs) {
         var expandImg = document.getElementById("expandedImg");
         var imgText = document.getElementById("imgtext");
         expandImg.src = imgs.src;
         imgText.innerHTML = imgs.alt;
         expandImg.parentElement.style.display = "block";
         }
         </script>

         </body>
         </html>

         """,height = 500)

def page2():
   st.write("Here is page 2.")
   if st.button("Button3"):
        st.write("Button1 clicked")


def page3():
      st.write("Here is page 3.")
      # ボタン
      st.button('ラベル')

      # チェックボックス
      st.checkbox('ラベル', value=False) # valueは初期状態

      # ラジオボタン
      st.radio("ラベル",('選択肢1', '選択肢2', '選択肢3'))

      # 選択肢
      st.selectbox('ラベル',('選択肢1', '選択肢2', '選択肢3'))

      # 複数選択
      st.multiselect('ラベル', ['選択肢1', '選択肢2', '選択肢3'],['選択肢2']) #例

      # スライダー
      #st.slider('ラベル', 最小値, 最大値, 初期値, 刻み値, フォーマット %d,%fなど)

      # テキスト入力
      st.text_input('ラベル', '初期表示文字列')

      # 数値入力
      st.number_input('ラベル',2, 5, 2)

      # ファイルアップロード
      #st.file_uploader("ラベル", type=ファイルタイプ,encoding) 
      # 上限ファイルサイズ200MB, ファイルタイプはcsvやpngなどをstrかlistで与える

def page4():
      st.write("Here is page 4.")
      
      st.title('タイトル：テスト')

      # サイドバー
      # ファイルアップロード
      uploaded_file = st.sidebar.file_uploader("ファイルアップロード", type='csv') 

      # グラフx軸設定
      x_axis = st.sidebar.selectbox('x軸項目',('材料A添加量', '材料B添加量', '材料C添加量'))


      # メイン画面
      st.header('読み込みデータ表示')
      if uploaded_file is not None:
            # アップロードファイルをメイン画面にデータ表示
            df = pd.read_csv(uploaded_file)
            st.write(df)

            # 選ばれたx軸の値からグラフ化
            st.header('グラフ表示')
            fig = px.scatter(x=df[x_axis], y=df['引張強度'])
            st.plotly_chart(fig, use_container_width=True)



if st.sidebar.button("Button-1"):
   page1()

if st.sidebar.button("Button-2"):
   page2()

if st.sidebar.button("Button-3"):
   page3()

if st.sidebar.button("Button-4"):
   page4()


