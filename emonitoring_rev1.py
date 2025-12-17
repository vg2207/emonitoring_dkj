# # IMPORT LIBRARY
# import streamlit as st
# import pandas as pd
# import numpy as np
# import os
# import xlsxwriter
# # import base64
# from datetime import datetime
# import cv2
# from PIL import Image
# from io import BytesIO
# import time
# from streamlit_extras.stylable_container import stylable_container


# def collect_image(nama_layar):
#     datetime_now = datetime.now()
#     date_number = datetime_now.strftime('%Y-%m-%d')
#     time = datetime_now.strftime('%H')+'-'+datetime_now.strftime('%M')+'-'+datetime_now.strftime('%S')
#     file_name = str(nama_layar) + ' - ' + str(date_number) + ' ' + str(time) + '.jpg'
#     path_to_save = os.path.join(os.getcwd(), 'saved_image')

#     if not os.path.exists(path_to_save):
#         os.makedirs(path_to_save)

#     return path_to_save, file_name

# def save_image(image, path_to_save, file_name):

#     bytes_data = image.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#     result_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
#     img_pil = Image.fromarray(result_img)
#     img_pil.save(os.path.join(path_to_save, file_name), "JPEG")

#     return img_pil, path_to_save, file_name

# def save_data(df):
#     path_to_save_data = os.path.join(os.getcwd(), 'output_data_emonitoring')

#     if not os.path.exists(path_to_save_data):
#         os.makedirs(path_to_save_data)
#         new_df = df.copy()
        
#         output = BytesIO()
#         with pd.ExcelWriter(output, engine='xlsxwriter') as writer: 
#             new_df = new_df.to_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name="Sheet1", startrow=0, header=True, index=False)
    
#     else:
#         df_exist = pd.read_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name='Sheet1', parse_dates=False)
#         new_df = pd.concat([df_exist, df])

#         output = BytesIO()
#         with pd.ExcelWriter(output, engine='xlsxwriter') as writer: 
#             new_df = new_df.to_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name="Sheet1", startrow=0, header=True, index=False)

#     return new_df



# def scroll_to_top():
#     scroll_js = """
#         <script>
#         const main = window.parent.document.querySelector('section.main');
#         if (main) {
#             main.scrollTo({ top: 0, behavior: 'smooth' });
#         }
#         </script>
#     """
#     container = st.empty()
#     container.markdown(scroll_js, unsafe_allow_html=True)
#     time.sleep(0.5)
#     container.empty()
    


# st.cache_data.clear()
# if "initialized" not in st.session_state:
#     st.session_state.clear()  # Clears everything
#     for key in list(st.session_state.keys()):
#         del st.session_state[key]
#     st.session_state.initialized = True  # Set a flag to prevent repeated clearing



# # col_0_1, col_0_2, col_0_3 = st.columns([1, 3, 1])
# # with col_0_1 :
# logo = Image.open('assets_logo/Logo Dunia Kimia Jaya.png')
# # with col_0_2 :
# # logo = Image.open("D:\Coding\Project Form Monitoring\Logo\logo.jpg")
# # logo = Image.open("D:\Coding\Project Form Monitoring\Logo\logo.jpg")
# # col_00, col_01, col_02 = st.columns([1, 3, 1])
# # with col_01:
# #     st.image(logo)

# st.logo(logo, size="large")

# df_produk = pd.read_excel("D:\Coding\Project Form Monitoring\Database Class Masterbatch.xlsx")
# produk_options = df_produk.iloc[:,2].dropna().tolist()

# # Halaman Awal

# if "page" not in st.session_state:
#     st.session_state["page"] = 0

# if st.session_state["page"] == 0 :
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
    
#     col_00, col_01, col_02 = st.columns([1, 3, 1])
#     with col_01:
#         st.image(logo)
    
#     st.markdown(f"<h2 style='text-align: center;'>WELCOME TO E-MONITORING PRODUKSI<br>DUNIA KIMIA JAYA</h2>", unsafe_allow_html=True)
#     st.markdown("""---""")
    
#     left_0, middle_0, right_0 = st.columns(3)
#     with middle_0:
#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             tombol_mulai = st.button(type="primary", label='Mulai', width="stretch")
#     if tombol_mulai:
#         st.session_state.page = 1
#         st.session_state.scroll_to_top = True
#         st.rerun()
        
        

# # Halaman 1
# if st.session_state["page"] == 1:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False

     
    
#     st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 1/6 : DATA UMUM</h3>", unsafe_allow_html=True)

#     with st.form(key='form_page_1', clear_on_submit=False):
#         nama_operator = st.text_input("Nama Operator", key="nama_operator")
        
#         with st.container(horizontal=True):
#             machine_options = ["Lab","E01", "E02", "E03", "E05", "E06"]
#             machine_selected_options = st.radio('Mesin', machine_options, key="machine_selected_options")
            
#             shift_options = ["1", "2", "3"]
#             shift_selected_options = st.radio('Shift', shift_options, key="shift_selected_options")
            
#             group_options = ["Kuning", "Hijau", "Merah", "Biru"]
#             group_selected_options = st.radio('Grup', group_options, key="group_selected_options")
            
#         with st.container(horizontal=True):
#             date_input = st.date_input("Tanggal Pengisian")
#             time_input = st.time_input("Jam Pengisian",step=3600)
            
#         nama_produk = st.selectbox(
#         "Nama Produk",
#         produk_options,
#         key="nama_produk",
#         index=None,
#         placeholder="Ketik nama produk..."
#         ) 

#         # (Tuliskan angka belakang dan huruf lengkap dibelakang angka saja, CONTOH : Untuk produk ASITHYLEN P White 9440 A, cukup tuliskan : 9440 A)
        
#         kondisi_mesin_options = ["Running", "Stop"]
#         kondisi_mesin_selected_options = st.pills('Kondisi Mesin', options=kondisi_mesin_options, key="kondisi_mesin_selected_options")

#         can_submit = True

#         if not nama_operator:
#             can_submit = False
#         if not machine_selected_options:
#             can_submit = False
#         if not shift_selected_options:
#             can_submit = False
#         if not group_selected_options:
#             can_submit = False
#         if not date_input:
#             can_submit = False
#         if not time_input:
#             can_submit = False
#         if not nama_produk:
#             can_submit = False
#         if not kondisi_mesin_selected_options:
#             can_submit = False

#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_1_1 = st.form_submit_button(label='Submit', width = "stretch")
                
#         if submit_button_1_1:
#             if can_submit == False:
#                 if not nama_operator:
#                     st.toast('Isi bagian "Nama Operator"!', icon="⚠️")
#                 if not machine_selected_options:
#                     st.toast('Isi bagian "Mesin"!', icon="⚠️")
#                 if not shift_selected_options:
#                     st.toast('Isi bagian "Shift"!', icon="⚠️")
#                 if not group_selected_options:
#                     st.toast('Isi bagian "Grup"!', icon="⚠️")
#                 if not date_input:
#                     st.toast('Isi bagian "Tanggal Pengisian"!', icon="⚠️")
#                 if not time_input:
#                     st.toast('Isi bagian "Jam Pengisian"!', icon="⚠️")
#                 if not nama_produk:
#                     st.toast('Isi bagian "Nama Produk"!', icon="⚠️")
#                 if not kondisi_mesin_selected_options:
#                     st.toast('Isi bagian "Kondisi Mesin"!', icon="⚠️")

#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")   
                
#             else:
#                 nama_kolom_page_1 = {
#                     "Nama Operator": [], 
#                     "Mesin": [], 
#                     "Shift": [], 
#                     "Tanggal Pengisian": [], 
#                     "Jam Pengisian": [],
#                     "Nama Produk": [],
#                     "Kondisi Mesin": []
#                     }
#                 df_data_page_1 = pd.DataFrame(nama_kolom_page_1)
#                 new_row_page_1 = pd.DataFrame(
#                 {"Nama Operator": [nama_operator],
#                 "Mesin": [machine_selected_options],
#                 "Shift": [shift_selected_options],
#                 "Tanggal Pengisian": [date_input],
#                 "Jam Pengisian": [time_input],
#                 "Nama Produk": [nama_produk],
#                 "Kondisi Mesin": [kondisi_mesin_selected_options]
#                 })
#                 df_data_page_1 = pd.concat([df_data_page_1, new_row_page_1]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_1.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_1 = df_data_page_1


#     left_1, middle_1, right_1 = st.columns([1,3,1])
#     with right_1:
#         submit_button_1_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
                
#     if submit_button_1_2:
#         if "df_data_page_1" not in st.session_state:
#             # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#         else:
#             if st.session_state.df_data_page_1["Kondisi Mesin"][0] == "Stop":
#                 st.session_state.page = 5   # langsung lompat ke halaman 5
#             else:
#                 st.session_state.page = 1.5   # kalau Running, lanjut normal ke halaman 2
#             st.session_state.scroll_to_top = True
#             st.rerun()
        

        

# # Halaman 1.5 - Pilih Feeder
# if st.session_state["page"] == 1.5:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
     
       
#     st.markdown("<h3 style='text-align: left;'><br>HALAMAN 2/6 : PILIH FEEDER YANG DIGUNAKAN</h3>", unsafe_allow_html=True)

#     with st.form(key='form_page_1_5', clear_on_submit=False):

#         feeder_options = [
#             "Feeder 1 - F1",
#             "Feeder 2 - F2",
#             "Feeder 3 - F3",
#             "Feeder 4 - F4",
#             "Feeder Jotam S50",
#             "Feeder Jotam S90 Resin",
#             "Feeder Jotam S90 Aditif",
#             "Liquid Feeder",
#             "Main Feeder",
#             "Side Feeder",
#             "Feeder Rework"
#         ]

#         selected_feeders = st.multiselect(
#             "Pilih feeder yang digunakan:",
#             feeder_options,
#             key="selected_feeders"
#         )

#         can_submit = True

#         if not selected_feeders:
#             can_submit = False

#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_1_1_5 = st.form_submit_button(label='Submit', width = "stretch")
#         if submit_button_1_1_5:
#             if can_submit == False:
#                 if not selected_feeders:
#                     st.toast('Isi bagian "Feeder yang digunakan"!', icon="⚠️")
#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")                
#             else:
#                 nama_kolom_page_1_5 = {
#                     "Feeder yang digunakan": []
#                     }
#                 df_data_page_1_5 = pd.DataFrame(nama_kolom_page_1_5)
#                 new_row_page_1_5 = pd.DataFrame(
#                 {"Feeder yang digunakan": [selected_feeders]
#                 })
#                 df_data_page_1_5 = pd.concat([df_data_page_1_5, new_row_page_1_5]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_1_5.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_1_5 = df_data_page_1_5



#     with st.container(horizontal=True):
#         back_button_1_5 = st.button("◀️ Kembali", width="stretch")
#         submit_button_1_2_5 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
        
#     if submit_button_1_2_5:
#         if "df_data_page_1_5" not in st.session_state:
#             # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#             # time.sleep(2)
#         else:
#             st.session_state.page = 2   # kalau Running, lanjut normal ke halaman 2
#             st.session_state.scroll_to_top = True
#             st.rerun()


    
    
        
#     @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
#     def backpage_1_5():
#         with st.container(horizontal=True):
#             button_no_1_5 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_1_5 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_1_5:
#                 if 'df_data_page_1_5' in st.session_state:
#                     del st.session_state['df_data_page_1_5']
#                 del st.session_state['df_data_page_1']
#                 st.session_state.page = 1
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_1_5:
#                 st.rerun()

        
#     if back_button_1_5:
#         backpage_1_5()
        
            


# #Halaman 2
# if st.session_state["page"] == 2:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False

     
    
#     df_data_page_1 = st.session_state.df_data_page_1
#     df_data_page_1_5 = st.session_state.df_data_page_1_5
#     st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 3/6 : MESIN FEEDER</h3>", unsafe_allow_html=True)


#     with st.form(key='form_page_2', clear_on_submit=False):
#         #Inisialisasi semua parameter sebelum proses pengondisian menggunakan fungsi IF
#         set_output_feeder_1 = None
#         actual_output_feeder_1 = None
#         set_output_feeder_2 = None
#         actual_output_feeder_2 = None
#         set_output_feeder_3 = None
#         actual_output_feeder_3 = None
#         set_output_feeder_4 = None
#         actual_output_feeder_4 = None
#         set_output_feeder_jotam_s50 = None
#         actual_output_feeder_jotam_s50 = None
#         set_output_feeder_jotam_s90_resin = None
#         actual_output_feeder_jotam_s90_resin = None
#         set_output_feeder_jotam_s90_aditif = None
#         actual_output_feeder_jotam_s90_aditif = None
#         set_output_liquid_feeder = None
#         actual_output_liquid_feeder = None
#         tekanan_liquid_feeder = None
#         ampere_main_feeder = None
#         rpm_main_feeder = None
#         rpm_side_feeder = None
#         rpm_feeder_rework = None
        
        
#         if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder 1 - F1 (kg/jam)</h5>", unsafe_allow_html=True)
                
#                 with st.container(horizontal=True):
#                     set_output_feeder_1 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_1", format="%d", step=1)
#                     actual_output_feeder_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_1", format="%d", step=1)
#         else:
#             set_output_feeder_1 = None
#             actual_output_feeder_1 = None
        
    
        
    
#         if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]: 
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder 2 - F2 (kg/jam)</h5>", unsafe_allow_html=True)
                
#                 with st.container(horizontal=True):
#                     set_output_feeder_2 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_2", format="%d", step=1)
#                     actual_output_feeder_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_2", format="%d", step=1)
#         else:
#             pass
    
#         if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]: 
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder 3 - F3 (kg/jam)</h5>", unsafe_allow_html=True)
                
#                 with st.container(horizontal=True):
#                     set_output_feeder_3 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_3", format="%d", step=1)
#                     actual_output_feeder_3 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_3", format="%d", step=1)
#         else:
#             pass
    
#         if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder 4 - F4 (kg/jam)</h5>", unsafe_allow_html=True)
                
#                 with st.container(horizontal=True):
#                     set_output_feeder_4 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_4", format="%d", step=1)
#                     actual_output_feeder_4 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_4", format="%d", step=1)
#         else :
#             pass
    
#         if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S50 (kg/jam)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_output_feeder_jotam_s50 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s50", format="%d", step=1)
#                     actual_output_feeder_jotam_s50 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s50", format="%d", step=1)
#         else :
#             pass
    
#         if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Resin (kg/jam)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_output_feeder_jotam_s90_resin = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s90_resin", format="%d", step=1)
#                     actual_output_feeder_jotam_s90_resin = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s90_resin", format="%d", step=1)
#         else :
#             pass
    
#         if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Aditif (kg/jam)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_output_feeder_jotam_s90_aditif = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s90_aditif", format="%d", step=1)
#                     actual_output_feeder_jotam_s90_aditif = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s90_aditif", format="%d", step=1)
#         else :
#             pass
    
#         if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Liquid Feeder (kg/jam)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_output_liquid_feeder = st.number_input("Set Point", value=None, placeholder="", key="set_output_liquid_feeder", format="%d", step=1)
#                     actual_output_liquid_feeder = st.number_input("Aktual", value=None, placeholder="", key="actual_output_liquid_feeder", format="%d", step=1)
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Tekanan Liquid Feeder</h5>", unsafe_allow_html=True)
#                 tekanan_liquid_feeder = st.number_input("Tekanan Liquid Feeder", value=None, placeholder="", key="tekanan_liquid_feeder", format="%d", step=1)
#         else :
#             pass
    
#         if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Main Feeder / Feeder 1</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#                         rpm_main_feeder = st.number_input("RPM main feeder", value=None, placeholder="", key="rpm_main_feeder", format="%d", step=1)
#                     else :
#                         pass
#                     if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
#                         ampere_main_feeder = st.number_input("Ampere main feeder", value=None, placeholder="", key="ampere_main_feeder", format="%0.1f", step=0.1)
#                     else :
#                         pass
#         else:
#             pass
    
#         if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Feeder Rework</h5>", unsafe_allow_html=True)
#                 rpm_feeder_rework = st.number_input("RPM feeder rework", value=None, placeholder="", key="rpm_feeder_rework", format="%d", step=1)
#         else :
#             pass
    
#         if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Side Feeder</h5>", unsafe_allow_html=True)
#                 rpm_side_feeder = st.number_input("RPM side feeder", value=None, placeholder="", key="rpm_side_feeder", format="%d", step=1)
#         else :
#             pass
        
#         can_submit = True
        
#         if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_1 is None:
#                 can_submit = False
#             if actual_output_feeder_1 is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_2 is None:
#                 can_submit = False
#             if actual_output_feeder_2 is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_3 is None:
#                 can_submit = False
#             if actual_output_feeder_3 is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_4 is None:
#                 can_submit = False
#             if actual_output_feeder_4 is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_jotam_s50 is None:
#                 can_submit = False
#             if actual_output_feeder_jotam_s50 is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_jotam_s90_resin is None:
#                 can_submit = False
#             if actual_output_feeder_jotam_s90_resin is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_feeder_jotam_s90_aditif is None:
#                 can_submit = False
#             if actual_output_feeder_jotam_s90_aditif is None:
#                 can_submit = False
#         else:
#             pass
    
#         if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if set_output_liquid_feeder is None:
#                 can_submit = False
#             if actual_output_liquid_feeder is None:
#                 can_submit = False
#             if tekanan_liquid_feeder is None:
#                 can_submit = False
#         else :
#             pass
    
#         if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#                 if rpm_main_feeder is None:
#                     can_submit = False
#             if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
#                 if ampere_main_feeder is None:
#                     can_submit = False

#         else :
#             pass
    
#         if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if rpm_feeder_rework is None:
#                 can_submit = False
#         else :
#             pass
    
#         if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#             if rpm_side_feeder is None:
#                 can_submit = False
#         else :
#             pass

        
#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_2_1 = st.form_submit_button(label='Submit', width = "stretch")
        
    
#         if submit_button_2_1:
#             if can_submit == False:
#                 if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_1 is None:
#                         st.toast('Isi bagian "Set Point Output Feeder 1 - F1"!', icon="⚠️")
#                     if actual_output_feeder_1 is None:
#                         st.toast('Isi bagian "Aktual Output Feeder 1 - F1"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_2 is None:
#                         st.toast('Isi bagian "Set Point Output Feeder 2 - F2"!', icon="⚠️")
#                     if actual_output_feeder_2 is None:
#                         st.toast('Isi bagian "Aktual Output Feeder 2 - F2"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_3 is None:
#                         st.toast('Isi bagian "Set Point Output Feeder 3 - F3"!', icon="⚠️")
#                     if actual_output_feeder_3 is None:
#                         st.toast('Isi bagian "Aktual Output Feeder 3 - F3"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_4 is None:
#                         st.toast('Isi bagian "Set Point Output Feeder 4 - F4"!', icon="⚠️")
#                     if actual_output_feeder_4 is None:
#                         st.toast('Isi bagian "Aktual Output Feeder 4 - F4"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_jotam_s50 is None:
#                         st.toast('Isi bagian "Set Point Output Feeder Jotam S50"!', icon="⚠️")
#                     if actual_output_feeder_jotam_s50 is None:
#                         st.toast('Isi bagian "Aktual Output Feeder Jotam S50"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_jotam_s90_resin is None:
#                         st.toast('Isi bagian "Set Point Output Feeder Jotam S90 Resin"!', icon="⚠️")
#                     if actual_output_feeder_jotam_s90_resin is None:
#                         st.toast('Isi bagian "Aktual Output Feeder Jotam S90 Resin"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_feeder_jotam_s90_aditif is None:
#                         st.toast('Isi bagian "Set Point Output Feeder Jotam S90 Aditif"!', icon="⚠️")
#                     if actual_output_feeder_jotam_s90_aditif is None:
#                         st.toast('Isi bagian "Aktual Output Feeder Jotam S90 Aditif"!', icon="⚠️")
#                 else:
#                     pass
            
#                 if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if set_output_liquid_feeder is None:
#                         st.toast('Isi bagian "Set Point Output Liquid Feeder"!', icon="⚠️")
#                     if actual_output_liquid_feeder is None:
#                         st.toast('Isi bagian "Aktual Output Liquid Feeder"!', icon="⚠️")
#                     if tekanan_liquid_feeder is None:
#                         st.toast('Isi bagian "Tekanan Liquid Feeder"!', icon="⚠️")
#                 else :
#                     pass
            
#                 if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#                         if rpm_main_feeder is None:
#                             st.toast('Isi bagian "RPM main feeder"!', icon="⚠️")
#                     if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
#                         if ampere_main_feeder is None:
#                             st.toast('Isi bagian "Ampere main feeder"!', icon="⚠️")
#                 else :
#                     pass
            
#                 if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if rpm_feeder_rework is None:
#                         st.toast('Isi bagian "RPM Feeder Rework"!', icon="⚠️")
#                 else :
#                     pass
            
#                 if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
#                     if rpm_side_feeder is None:
#                         st.toast('Isi bagian "RPM Side Feeder"!', icon="⚠️")
#                 else :
#                     pass
                    
#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
#             else:
#                 nama_kolom_page_2 = {
#                     "Set Point Output Feeder 1 - F1 (kg/jam)": [], 
#                     "Aktual Output Feeder 1 - F1 (kg/jam)": [], 
#                     "Set Point Output Feeder 2 - F2 (kg/jam)": [], 
#                     "Aktual Output Feeder 2 - F2 (kg/jam)": [], 
#                     "Set Point Output Feeder 3 - F3 (kg/jam)": [], 
#                     "Aktual Output Feeder 3 - F3 (kg/jam)": [], 
#                     "Set Point Output Feeder 4 - F4 (kg/jam)": [], 
#                     "Aktual Output Feeder 4 - F4 (kg/jam)": [], 
#                     "Set Point Output Feeder Jotam S50 (kg/jam)": [], 
#                     "Aktual Output Feeder Jotam S50 (kg/jam)": [], 
#                     "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [], 
#                     "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [], 
#                     "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
#                     "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
#                     "Set Point Output Liquid Feeder (kg/jam)": [], 
#                     "Aktual Output Liquid Feeder (kg/jam)": [], 
#                     "Tekanan Liquid Feeder": [], 
#                     "RPM Main Feeder": [], 
#                     "Ampere Main Feeder": [], 
#                     "RPM Feeder Rework": [], 
#                     "RPM Side Feeder": [] 
#                     }
#                 df_data_page_2 = pd.DataFrame(nama_kolom_page_2)
    
#                 new_row_page_2 = pd.DataFrame({
#                     "Set Point Output Feeder 1 - F1 (kg/jam)": [set_output_feeder_1], 
#                     "Aktual Output Feeder 1 - F1 (kg/jam)": [actual_output_feeder_1], 
#                     "Set Point Output Feeder 2 - F2 (kg/jam)": [set_output_feeder_2], 
#                     "Aktual Output Feeder 2 - F2 (kg/jam)": [actual_output_feeder_2], 
#                     "Set Point Output Feeder 3 - F3 (kg/jam)": [set_output_feeder_3], 
#                     "Aktual Output Feeder 3 - F3 (kg/jam)": [actual_output_feeder_3], 
#                     "Set Point Output Feeder 4 - F4 (kg/jam)": [set_output_feeder_4], 
#                     "Aktual Output Feeder 4 - F4 (kg/jam)": [actual_output_feeder_4], 
#                     "Set Point Output Feeder Jotam S50 (kg/jam)": [set_output_feeder_jotam_s50], 
#                     "Aktual Output Feeder Jotam S50 (kg/jam)": [actual_output_feeder_jotam_s50], 
#                     "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [set_output_feeder_jotam_s90_resin], 
#                     "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [actual_output_feeder_jotam_s90_resin], 
#                     "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [set_output_feeder_jotam_s90_aditif], 
#                     "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [actual_output_feeder_jotam_s90_aditif], 
#                     "Set Point Output Liquid Feeder (kg/jam)": [set_output_liquid_feeder], 
#                     "Aktual Output Liquid Feeder (kg/jam)": [actual_output_liquid_feeder], 
#                     "Tekanan Liquid Feeder": [tekanan_liquid_feeder], 
#                     "RPM Main Feeder": [rpm_main_feeder], 
#                     "Ampere Main Feeder": [ampere_main_feeder], 
#                     "RPM Feeder Rework": [rpm_feeder_rework], 
#                     "RPM Side Feeder": [rpm_side_feeder] 
#                 })
#                 df_data_page_2 = pd.concat([df_data_page_2, new_row_page_2]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_2.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_2 = df_data_page_2
                

#     with st.container(horizontal=True):
#         back_button_2 = st.button("◀️ Kembali", width="stretch")
#         submit_button_2_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
#     if submit_button_2_2:
#         if "df_data_page_2" not in st.session_state:
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#         else:
#             st.session_state.page = 3
#             st.session_state.scroll_to_top = True
#             st.rerun()
            
        
        
#     @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
#     def backpage_2():
#         with st.container(horizontal=True):
#             button_no_2 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_2 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_2:
#                 if 'df_data_page_2' in st.session_state:
#                     del st.session_state['df_data_page_2']
#                 del st.session_state['df_data_page_1_5']
#                 st.session_state.page = 1.5  # kembali ke halaman 1.5
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_2:
#                 st.rerun()

        
#     if back_button_2:
#         backpage_2()
        
            
                
        
        

# #Halaman 3
# if st.session_state["page"] == 3:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
     
    
#     df_data_page_1 = st.session_state.df_data_page_1
#     st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 4/6 : EXTRUDER</h3>", unsafe_allow_html=True)
#     # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
#     # st.write(df_all_data)

#     with st.form(key='form_page_3', clear_on_submit=False):

#         foto_mesin_base64 = None
#         set_output_mesin_extruder = None
#         actual_output_mesin_extruder = None 
#         set_ampere_RPM_extruder = None
#         actual_ampere_RPM_extruder = None
#         specific_energy_index = None
#         set_melt_temperature_extruder = None
#         set_melt_pressure_extruder = None
#         valve_condition_options = None
#         set_temperature_zone_1 = None
#         actual_temperature_zone_1 = None
#         set_temperature_zone_2 = None
#         actual_temperature_zone_2 = None
#         set_temperature_zone_3 = None
#         actual_temperature_zone_3 = None
#         set_temperature_zone_4 = None
#         actual_temperature_zone_4 = None
#         set_temperature_zone_5 = None
#         actual_temperature_zone_5 = None
#         set_temperature_zone_6 = None
#         actual_temperature_zone_6 = None
#         set_temperature_zone_7 = None
#         actual_temperature_zone_7 = None
#         set_temperature_zone_8 = None
#         actual_temperature_zone_8 = None
#         set_temperature_zone_9 = None
#         actual_temperature_zone_9 = None
#         set_temperature_zone_10 = None
#         actual_temperature_zone_10 = None
#         set_temperature_zone_11 = None
#         actual_temperature_zone_11 = None
#         set_temperature_zone_12 = None
#         actual_temperature_zone_12 = None
#         set_temperature_8 = None
#         actual_temperature_8 = None
#         set_temperature_input_screen_changer = None
#         actual_temperature_input_screen_changer = None
#         set_temperature_TSW_screen_changer_1 = None
#         actual_temperature_TSW_screen_changer_1 = None
#         set_temperature_screen_changer_2 = None
#         actual_temperature_screen_changer_2 = None
#         temperature_cooling_barrel_mesin = None
#         temperature_gearbox_cooling = None
#         pressure_cooling_barrel_mesin = None
#         temperature_gearbox_oil = None
#         pressure_gearbox_oil = None
#         vacuum_bar_value = None
#         pressure_vacuum_system_water = None

#         st.markdown(f"<h5 style='text-align: left;'>📷 Dokumentasi Panel Mesin Extruder</h5>", unsafe_allow_html=True)
#         foto_mesin = st.camera_input("Ambil foto panel mesin extruder", key="foto_mesin")
#         if foto_mesin is not None:
#             path_to_save_extruder, file_name_extruder = collect_image(nama_layar = 'extruder')

#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Output Mesin (kg/jam)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_output_mesin_extruder = st.number_input("Set Point", value=None, placeholder="", key="set_output_mesin_extruder", format="%d", step=1)
#                     actual_output_mesin_extruder = st.number_input("Aktual", value=None, placeholder="", key="actual_output_mesin_extruder", format="%d", step=1)
#         else : 
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Ampere & RPM Extruder</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 set_ampere_RPM_extruder = st.number_input("Ampere/Torsi", value=None, placeholder="", key="set_ampere_RPM_extruder")
#                 actual_ampere_RPM_extruder = st.number_input("RPM", value=None, placeholder="", key="actual_ampere_RPM_extruder", format="%d", step=1)

#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>SEI (KWh/kg)</h5>", unsafe_allow_html=True)
#                 specific_energy_index = st.number_input("SEI", key="specific_energy_index", format="%0.2f", step=0.01)
#         else :
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Melt Temperature - Pressure Ekstruder</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     set_melt_temperature_extruder = st.number_input("Set Melt Temperature", value=None, placeholder="", key="set_melt_temperature_extruder", format="%d", step=1)
#                 else : 
#                     pass
    
#                 set_melt_pressure_extruder = st.number_input("Set Melt Pressure", value=None, placeholder="", key="set_melt_pressure_extruder", format="%d", step=1)
   
#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Kondisi Valve Pendingin Barrel Zone 1</h5>", unsafe_allow_html=True)
#                 valve_condition_options = ["OPEN", "CLOSE"]
#                 valve_condition_options = st.radio('', valve_condition_options, key="valve_condition_options")
#         else :
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 1</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#                     set_temperature_zone_1 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_1", format="%d", step=1)
#                 else :
#                     pass

#                 actual_temperature_zone_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_1", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 2</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 set_temperature_zone_2 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_2", format="%d", step=1)
#                 actual_temperature_zone_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_2", format="%d", step=1)
        
#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 3</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 set_temperature_zone_3 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_3", format="%d", step=1)
#                 actual_temperature_zone_3 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_3", format="%d", step=1)
        
#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 4</h5>", unsafe_allow_html=True)
            
#             with st.container(horizontal=True):
#                 set_temperature_zone_4 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_4", format="%d", step=1)
#                 actual_temperature_zone_4 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_4", format="%d", step=1)
                
#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 5</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 set_temperature_zone_5 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_5", format="%d", step=1)
#                 actual_temperature_zone_5 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_5", format="%d", step=1)
        
#         if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 6</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_6 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_6", format="%d", step=1)
#                     actual_temperature_zone_6 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_6", format="%d", step=1)
            
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 7</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_7 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_7", format="%d", step=1)
#                     actual_temperature_zone_7 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_7", format="%d", step=1)
                    
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 8</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_8 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_8", format="%d", step=1)
#                     actual_temperature_zone_8 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_8", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 9</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_9 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_9", format="%d", step=1)
#                     actual_temperature_zone_9 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_9", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 10</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_10 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_10", format="%d", step=1)
#                     actual_temperature_zone_10 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_10", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 11</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_11 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_11", format="%d", step=1)
#                     actual_temperature_zone_11 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_11", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E03':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 12</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_zone_12 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_12", format="%d", step=1)
#                     actual_temperature_zone_12 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_12", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature 8.0</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_8 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_8", format="%d", step=1)
#                     actual_temperature_8 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_8", format="%d", step=1)
#         else :
#             pass
        
#         if df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Input Screen Changer</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_input_screen_changer = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_input_screen_changer", format="%d", step=1)
#                     actual_temperature_input_screen_changer = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_input_screen_changer", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature TSW / Screen Changer 1</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_TSW_screen_changer_1 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_TSW_screen_changer_1", format="%d", step=1)
#                     actual_temperature_TSW_screen_changer_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_TSW_screen_changer_1", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Screen Changer 2</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_screen_changer_2 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_screen_changer_2", format="%d", step=1)
#                     actual_temperature_screen_changer_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_screen_changer_2", format="%d", step=1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Cooling Barrel Mesin (Soft Water)</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     if df_data_page_1["Mesin"][0] == 'E06':
#                         temperature_cooling_barrel_mesin = st.number_input("Temperature Air Cooling Barrel", value=None, placeholder="TEMPERATURE", key="temperature_cooling_barrel_mesin", format="%d", step=1)
#                     else :
#                         pass
    
#                     pressure_cooling_barrel_mesin = st.number_input("Tekanan Air Cooling Barrel", value=None, placeholder="TEKANAN AIR", key="pressure_cooling_barrel_mesin", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Cooling Gearbox (Cooling Tower)</h5>", unsafe_allow_html=True)
#                 temperature_gearbox_cooling = st.number_input("Temperature Cooling Gearbox", value=None, placeholder="", key="temperature_gearbox_cooling", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Parameter Gearbox Mesin</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     temperature_gearbox_oil = st.number_input("Temperature Oli Gearbox", value=None, placeholder="", key="temperature_gearbox_oil", format="%d", step=1)
#                     pressure_gearbox_oil = st.number_input("Tekanan Oli Gearbox", value=None, placeholder="", key="pressure_gearbox_oil", format="%0.1f", step=0.1)
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Parameter Vacuum System</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     vacuum_bar_value = st.number_input("Vacuum Bar", value=None, placeholder="", key="vacuum_bar_value", format="%d", step=1)
#                     if df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E06':
#                         pressure_vacuum_system_water = st.number_input("Tekanan Air Vacuum System", value=None, placeholder="", key="pressure_vacuum_system_water", format="%0.1f", step=0.1)
#                     else :
#                         pass
#         else:
#             pass


        
#         can_submit = True

#         if foto_mesin is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if set_output_mesin_extruder is None:
#                 can_submit = False
#             if actual_output_mesin_extruder is None:
#                 can_submit = False
#         else : 
#             pass

#         if set_ampere_RPM_extruder is None:
#             can_submit = False
#         if actual_ampere_RPM_extruder is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if specific_energy_index is None:
#                 can_submit = False
#         else : 
#             pass

#         if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02'or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if set_melt_temperature_extruder is None:
#                 can_submit = False
#         else :
#             pass

#         if set_melt_pressure_extruder is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if valve_condition_options is None:
#                 can_submit = False
#         else :
#             pass
        
#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#             if set_temperature_zone_1 is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if actual_temperature_zone_1 is None:
#                 can_submit = False
#             if set_temperature_zone_2 is None:
#                 can_submit = False
#             if actual_temperature_zone_2 is None:
#                 can_submit = False
#             if set_temperature_zone_3 is None:
#                 can_submit = False
#             if actual_temperature_zone_3 is None:
#                 can_submit = False
#             if set_temperature_zone_4 is None:
#                 can_submit = False
#             if actual_temperature_zone_4 is None:
#                 can_submit = False
#             if set_temperature_zone_5 is None:
#                 can_submit = False
#             if actual_temperature_zone_5 is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':    
#             if set_temperature_zone_6 is None:
#                 can_submit = False
#             if actual_temperature_zone_6 is None:
#                 can_submit = False
#             if set_temperature_zone_7 is None:
#                 can_submit = False
#             if actual_temperature_zone_7 is None:
#                 can_submit = False
#             if set_temperature_zone_8 is None:
#                 can_submit = False
#             if actual_temperature_zone_8 is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if set_temperature_zone_9 is None:
#                 can_submit = False
#             if actual_temperature_zone_9 is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if set_temperature_zone_10 is None:
#                 can_submit = False
#             if actual_temperature_zone_10 is None:
#                 can_submit = False
#         else : 
#             pass
        
#         if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
#             if set_temperature_zone_11 is None:
#                 can_submit = False
#             if actual_temperature_zone_11 is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0]=='E03':
#             if set_temperature_zone_12 is None:
#                 can_submit = False
#             if actual_temperature_zone_12 is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0]=='E06':
#             if set_temperature_8 is None:
#                 can_submit = False
#             if actual_temperature_8 is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0]=='E05':
#             if set_temperature_input_screen_changer is None:
#                 can_submit = False
#             if actual_temperature_input_screen_changer is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0]=='E05' or df_data_page_1["Mesin"][0]=='E06':
#             if set_temperature_TSW_screen_changer_1 is None:
#                 can_submit = False
#             if actual_temperature_TSW_screen_changer_1 is None:
#                 can_submit = False
#         else :
#             pass
        
#         if df_data_page_1["Mesin"][0]=='E05':
#             if set_temperature_screen_changer_2 is None:
#                 can_submit = False
#             if actual_temperature_screen_changer_2 is None:
#                 can_submit = False
#         else :
#             pass
    
#         if df_data_page_1["Mesin"][0]=='E06':
#             if temperature_cooling_barrel_mesin is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0]=='E06' or df_data_page_1["Mesin"][0]=='E05':
#             if temperature_gearbox_cooling is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if pressure_cooling_barrel_mesin is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0]=='E06':
#             if temperature_gearbox_oil is None:
#                 can_submit = False
#             if pressure_gearbox_oil is None:
#                 can_submit = False
#         else :
#             pass

#         if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#             if vacuum_bar_value is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
#             if pressure_vacuum_system_water is None:
#                 can_submit = False
#         else :
#             pass

#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_3_1 = st.form_submit_button(label='Submit', width = "stretch")

#         if submit_button_3_1:
#             if can_submit == False:
#                 if foto_mesin is None:
#                     st.toast('Ambil foto panel extruder', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if set_output_mesin_extruder is None:
#                         st.toast('Isi bagian "Set Point Output Mesin"!', icon="⚠️")
#                     if actual_output_mesin_extruder is None:
#                         st.toast('Isi bagian "Aktual Output Mesin"!', icon="⚠️")
#                 else : 
#                     pass
        
#                 if set_ampere_RPM_extruder is None:
#                     st.toast('Isi bagian "Set Point Ampere & RPM Extruder"!', icon="⚠️")
#                 if actual_ampere_RPM_extruder is None:
#                     st.toast('Isi bagian "Aktual Ampere & RPM Extruder"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if specific_energy_index is None:
#                         st.toast('Isi bagian "SEI"!, icon="⚠️"')
#                 else : 
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02'or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if set_melt_temperature_extruder is None:
#                         st.toast('Isi bagian "Melt Temperature Extruder"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if set_melt_pressure_extruder is None:
#                     st.toast('Isi bagian "Melt Pressure Extruder"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if valve_condition_options is None:
#                         st.toast('Isi bagian "Kondisi Valve Pendingin Barrel Zone 1"!', icon="⚠️")
#                 else :
#                     pass
                
#                 if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
#                     if set_temperature_zone_1 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 1"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if actual_temperature_zone_1 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 1"!', icon="⚠️")
#                     if set_temperature_zone_2 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 2"!', icon="⚠️")
#                     if actual_temperature_zone_2 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 2"!', icon="⚠️")
#                     if set_temperature_zone_3 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 3"!', icon="⚠️")
#                     if actual_temperature_zone_3 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 3"!', icon="⚠️")
#                     if set_temperature_zone_4 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 4"!', icon="⚠️")
#                     if actual_temperature_zone_4 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 4"!', icon="⚠️")
#                     if set_temperature_zone_5 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 5"!', icon="⚠️")
#                     if actual_temperature_zone_5 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 5"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':    
#                     if set_temperature_zone_6 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 6"!', icon="⚠️")
#                     if actual_temperature_zone_6 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 6"!', icon="⚠️")
#                     if set_temperature_zone_7 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 7"!', icon="⚠️")
#                     if actual_temperature_zone_7 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 7"!', icon="⚠️")
#                     if set_temperature_zone_8 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 8"!', icon="⚠️")
#                     if actual_temperature_zone_8 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 8"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if set_temperature_zone_9 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 9"!', icon="⚠️")
#                     if actual_temperature_zone_9 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 9"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if set_temperature_zone_10 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 10"!', icon="⚠️")
#                     if actual_temperature_zone_10 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 10"!', icon="⚠️")
#                 else : 
#                     pass
                
#                 if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
#                     if set_temperature_zone_11 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 11"!', icon="⚠️")
#                     if actual_temperature_zone_11 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 11"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E03':
#                     if set_temperature_zone_12 is None:
#                         st.toast('Isi bagian "Set Point Temperature Zone 12"!', icon="⚠️")
#                     if actual_temperature_zone_12 is None:
#                         st.toast('Isi bagian "Aktual Temperature Zone 12"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E06':
#                     if set_temperature_8 is None:
#                         st.toast('Isi bagian "Set Point Temperature 8.0"!', icon="⚠️")
#                     if actual_temperature_8 is None:
#                         st.toast('Isi bagian "Aktual Temperature 8.0"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E05':
#                     if set_temperature_input_screen_changer is None:
#                         st.toast('Isi bagian "Set Point Temperature Input Screen Changer"!', icon="⚠️")
#                     if actual_temperature_input_screen_changer is None:
#                         st.toast('Isi bagian "Aktual Temperature Input Screen Changer"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E05' or df_data_page_1["Mesin"][0]=='E06':
#                     if set_temperature_TSW_screen_changer_1 is None:
#                         st.toast('Isi bagian "Set Point Temperature TSW / Screen Changer 1"!', icon="⚠️")
#                     if actual_temperature_TSW_screen_changer_1 is None:
#                         st.toast('Isi bagian "Aktual Temperature TSW / Screen Changer 1"!', icon="⚠️")
#                 else :
#                     pass
                
#                 if df_data_page_1["Mesin"][0]=='E05':
#                     if set_temperature_screen_changer_2 is None:
#                         st.toast('Isi bagian "Set Point Temperature Screen Changer 2"!', icon="⚠️")
#                     if actual_temperature_screen_changer_2 is None:
#                         st.toast('Isi bagian "Aktual Temperature Screen Changer 2"!', icon="⚠️")
#                 else :
#                     pass
            
#                 if df_data_page_1["Mesin"][0]=='E06':
#                     if temperature_cooling_barrel_mesin is None:
#                         st.toast('Isi bagian "Temperature Air Cooling Barrel Mesin (Soft Water)"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E06' or df_data_page_1["Mesin"][0]=='E05':
#                     if temperature_gearbox_cooling is None:
#                         st.toast('Isi bagian "Temperature Air Cooling Gearbox (Cooling Tower)"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if pressure_cooling_barrel_mesin is None:
#                         st.toast('Isi bagian "Tekanan Air Cooling Barrel Mesin"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E06':
#                     if temperature_gearbox_oil is None:
#                         st.toast('Isi bagian "Temperature Oli Gearbox"!', icon="⚠️")
#                     if pressure_gearbox_oil is None:
#                         st.toast('Isi bagian "Tekanan Oli Gearbox"!', icon="⚠️")
#                 else :
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
#                     if vacuum_bar_value is None:
#                         st.toast('Isi bagian "Vacuum Bar"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
#                     if pressure_vacuum_system_water is None:
#                         st.toast('Isi bagian "Tekanan Air Vacuum System"!', icon="⚠️")
#                 else :
#                     pass
                    
#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
#             else:
#                 nama_kolom_page_3 = {
#                     "Dokumentasi Panel Mesin Extruder":[],
#                     "Set Point Output Mesin": [], 
#                     "Aktual Output Mesin": [], 
#                     "Set Point Ampere & RPM Extruder": [], 
#                     "Aktual Ampere & RPM Extruder": [], 
#                     "SEI": [], 
#                     "Melt Temperature Extruder": [], 
#                     "Melt Pressure Extruder": [], 
#                     "Kondisi Valve Pendingin Barrel Zone 1": [], 
#                     "Set Point Temperature Zone 1": [], 
#                     "Aktual Temperature Zone 1": [],
#                     "Set Point Temperature Zone 2": [], 
#                     "Aktual Temperature Zone 2": [],
#                     "Set Point Temperature Zone 3": [], 
#                     "Aktual Temperature Zone 3": [], 
#                     "Set Point Temperature Zone 4": [], 
#                     "Aktual Temperature Zone 4": [],
#                     "Set Point Temperature Zone 5": [], 
#                     "Aktual Temperature Zone 5": [],
#                     "Set Point Temperature Zone 6": [], 
#                     "Aktual Temperature Zone 6": [],
#                     "Set Point Temperature Zone 7": [], 
#                     "Aktual Temperature Zone 7": [],
#                     "Set Point Temperature Zone 8": [], 
#                     "Aktual Temperature Zone 8": [],
#                     "Set Point Temperature Zone 9": [], 
#                     "Aktual Temperature Zone 9": [],
#                     "Set Point Temperature Zone 10": [], 
#                     "Aktual Temperature Zone 10": [],
#                     "Set Point Temperature Zone 11": [], 
#                     "Aktual Temperature Zone 11": [],
#                     "Set Point Temperature Zone 12": [], 
#                     "Aktual Temperature Zone 12": [],
#                     "Set Point Temperature 8.0": [], 
#                     "Aktual Temperature 8.0": [], 
#                     "Set Point Temperature Input Screen Changer": [], 
#                     "Aktual Temperature Input Screen Changer": [], 
#                     "Set Point Temperature TSW / Screen Changer 1": [], 
#                     "Aktual Temperature TSW / Screen Changer 1": [], 
#                     "Set Point Temperature Screen Changer 2": [], 
#                     "Aktual Temperature Screen Changer 2": [], 
#                     "Temperature Air Cooling Barrel Mesin (Soft Water)": [],
#                     "Temperature Air Cooling Gearbox (Cooling Tower)":[], 
#                     "Tekanan Air Cooling Barrel Mesin": [], 
#                     "Temperature Oli Gearbox": [] ,
#                     "Vacuum Bar": [],
#                     "Tekanan Air Vacuum System":[]
#                     }
#                 df_data_page_3 = pd.DataFrame(nama_kolom_page_3)

#                 new_row_page_3 = pd.DataFrame({
#                     # "Dokumentasi Panel Mesin Extruder": [foto_mesin_base64],
#                     "Dokumentasi Panel Mesin Extruder": [str(os.path.join(path_to_save_extruder, file_name_extruder))],
#                     "Set Point Output Mesin": [set_output_mesin_extruder], 
#                     "Aktual Output Mesin": [actual_output_mesin_extruder], 
#                     "Set Point Ampere & RPM Extruder": [set_ampere_RPM_extruder], 
#                     "Aktual Ampere & RPM Extruder": [actual_ampere_RPM_extruder], 
#                     "SEI": [specific_energy_index],
#                     "Melt Temperature Extruder": [set_melt_temperature_extruder], 
#                     "Melt Pressure Extruder": [set_melt_pressure_extruder], 
#                     "Kondisi Valve Pendingin Barrel Zone 1": [valve_condition_options], 
#                     "Set Point Temperature Zone 1": [set_temperature_zone_1], 
#                     "Aktual Temperature Zone 1": [actual_temperature_zone_1],
#                     "Set Point Temperature Zone 2": [set_temperature_zone_2], 
#                     "Aktual Temperature Zone 2": [actual_temperature_zone_2],
#                     "Set Point Temperature Zone 3": [set_temperature_zone_3], 
#                     "Aktual Temperature Zone 3": [actual_temperature_zone_3], 
#                     "Set Point Temperature Zone 4": [set_temperature_zone_4], 
#                     "Aktual Temperature Zone 4": [actual_temperature_zone_4],
#                     "Set Point Temperature Zone 5": [set_temperature_zone_5], 
#                     "Aktual Temperature Zone 5": [actual_temperature_zone_5],
#                     "Set Point Temperature Zone 6": [set_temperature_zone_6], 
#                     "Aktual Temperature Zone 6": [actual_temperature_zone_6],
#                     "Set Point Temperature Zone 7": [set_temperature_zone_7], 
#                     "Aktual Temperature Zone 7": [actual_temperature_zone_7],
#                     "Set Point Temperature Zone 8": [set_temperature_zone_8], 
#                     "Aktual Temperature Zone 8": [actual_temperature_zone_8],
#                     "Set Point Temperature Zone 9": [set_temperature_zone_9], 
#                     "Aktual Temperature Zone 9": [actual_temperature_zone_9],
#                     "Set Point Temperature Zone 10": [set_temperature_zone_10], 
#                     "Aktual Temperature Zone 10": [actual_temperature_zone_10],
#                     "Set Point Temperature Zone 11": [set_temperature_zone_11], 
#                     "Aktual Temperature Zone 11": [actual_temperature_zone_11],
#                     "Set Point Temperature Zone 12": [set_temperature_zone_12], 
#                     "Aktual Temperature Zone 12": [actual_temperature_zone_12],
#                     "Set Point Temperature 8.0": [set_temperature_8], 
#                     "Aktual Temperature 8.0": [actual_temperature_8], 
#                     "Set Point Temperature Input Screen Changer": [set_temperature_input_screen_changer], 
#                     "Aktual Temperature Input Screen Changer": [actual_temperature_input_screen_changer], 
#                     "Set Point Temperature TSW / Screen Changer 1": [set_temperature_TSW_screen_changer_1], 
#                     "Aktual Temperature TSW / Screen Changer 1": [actual_temperature_TSW_screen_changer_1], 
#                     "Set Point Temperature Screen Changer 2": [set_temperature_screen_changer_2], 
#                     "Aktual Temperature Screen Changer 2": [actual_temperature_screen_changer_2], 
#                     "Temperature Air Cooling Barrel Mesin (Soft Water)": [temperature_cooling_barrel_mesin], 
#                     "Tekanan Air Cooling Barrel Mesin": [pressure_cooling_barrel_mesin],
#                     "Temperature Air Cooling Gearbox (Cooling Water)": [temperature_gearbox_cooling], 
#                     "Temperature Oli Gearbox": [temperature_gearbox_oil],
#                     "Tekanan Oli Gearbox": [pressure_gearbox_oil],
#                     "Vacuum Bar": [vacuum_bar_value],
#                     "Tekanan Air Vacuum System":[pressure_vacuum_system_water] 
#                 })
#                 df_data_page_3 = pd.concat([df_data_page_3, new_row_page_3]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_3.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_3 = df_data_page_3
                
            

#     with st.container(horizontal=True) :
#         back_button_3 = st.button("◀️ Kembali", width="stretch")
#         submit_button_3_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
#     if submit_button_3_2:
#         if "df_data_page_3" not in st.session_state:
#             # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#             # time.sleep(2)
#         else:
#             foto_mesin, path_to_save_extruder, file_name_extruder = save_image(image = foto_mesin, path_to_save = path_to_save_extruder, file_name = file_name_extruder)
#             st.session_state.page = 4
#             st.session_state.scroll_to_top = True
#             st.rerun()
            
        
        
#     @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
#     def backpage_3():
#         with st.container(horizontal=True):
#             button_no_3 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_3 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_3:
#                 if 'df_data_page_3' in st.session_state:
#                     del st.session_state['df_data_page_3']
#                 del st.session_state['df_data_page_2']
#                 st.session_state.page = 2  # kembali ke halaman 1
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_3:
#                 st.rerun()

        
#     if back_button_3:
#         backpage_3()
        
        
        

# #Halaman 4
# if st.session_state["page"] == 4:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
     
    
#     df_data_page_1 = st.session_state.df_data_page_1
#     st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 5/6 : UWP-PELLETIZER</h3>", unsafe_allow_html=True)


#     with st.form(key='form_page_4', clear_on_submit=False):

#         set_temperature_adapter = None
#         actual_temperature_adapter = None
#         set_temperature_podv = None
#         actual_temperature_podv = None
#         set_temperature_die_plate = None
#         actual_temperature_die_plate = None
#         set_temperature_water_tank = None
#         actual_temperature_water_tank = None
#         melt_pressure_uwp = None
#         melt_temperature_uwp = None
#         die_plate_options = None
#         ampere_cutter = None
#         rpm_cutter = None
#         setting_cutter = None
#         percentage_cutter = None
#         uwp_water_pressure = None
#         uwp_water_flow = None
#         cutter_hub_options = None
#         mesh_screen_options = None
#         temperature_in_proses = None
#         temperature_out_proses = None
#         temperature_in_cooling_water = None
#         temperature_out_cooling_water = None
#         actual_output_finished_good = None
#         granule_number = None
#         die_hole_open_calc = None
#         foto_uwp = None
#         foto_uwp_path = None

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             st.markdown(f"<h5 style='text-align: left;'>📷 Dokumentasi Panel Underwater Pelletizer</h5>", unsafe_allow_html=True)
#             foto_uwp = st.camera_input("Ambil foto panel UWP", key="foto_uwp")
#             if foto_uwp is not None:
#                 path_to_save_uwp, file_name_uwp = collect_image(nama_layar = 'UWP')
#                 foto_uwp_path = str(os.path.join(path_to_save_uwp, file_name_uwp))

#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Adapter</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_adapter = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_adapter", format="%d", step=1)
#                     actual_temperature_adapter = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_adapter", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature PoDV</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_podv = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_podv", format="%d", step=1)
#                     actual_temperature_podv = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_podv", format="%d", step=1)
#         else:
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Temperature Die Plate</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 set_temperature_die_plate = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_die_plate", format="%d", step=1)
#                 actual_temperature_die_plate = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_die_plate", format="%d", step=1)

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Temperature Water Tank</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     set_temperature_water_tank = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_water_tank", format="%d", step=1)
#                     actual_temperature_water_tank = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_water_tank", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Melt Parameter pada UWP</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     melt_pressure_uwp = st.number_input("Melt Pressure", value=None, placeholder="", key="melt_pressure_uwp", format="%d", step=1)
#                     melt_temperature_uwp = st.number_input("Melt Temperature", value=None, placeholder="", key="melt_temperature_uwp", format="%d", step=1)
#         else:
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Jenis Die Plate</h5>", unsafe_allow_html=True)
#             die_plate_options = ["Lab; 2 hole","E01; 2.8 mm; 10 hole", "E02; 2 mm; 20 hole","E02; 3.5 mm; 17 hole","E02; 4 mm; 9 hole","E03; 2 mm; 20 hole",
#             "E03; 4 mm; 15 hole","E03; 3.5 mm; 7 hole","E05; 2.8 mm; 20 hole","E05; 2.8 mm; 10 hole","E05; 3.2 mm; 10 hole","E06; 2 mm; 48 hole",
#             "E06; 2.8 mm; 24 hole"]
#             die_plate_options = st.radio('', die_plate_options, key="die_plate_options")

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Cutter</h5>", unsafe_allow_html=True)
#             with st.container(horizontal=True):
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     ampere_cutter = st.number_input("Ampere/Torsi Cutter", value=None, placeholder="", key="ampere_cutter", format="%0.1f", step=0.1)
#                 else:
#                     pass
    
#                 rpm_cutter = st.number_input("RPM Cutter", value=None, placeholder="", key="rpm_cutter", format="%d", step=1)

            
#             if df_data_page_1["Mesin"][0] == 'E06':
#                 with st.container(horizontal=True):
#                     setting_cutter = st.number_input("Setting Maju Cutter", value=None, placeholder="", key="setting_cutter", format="%d", step=1)
#                     percentage_cutter = st.number_input("% Panjang Cutter", value=None, placeholder="", key="percentage_cutter", format="%d", step=1)
#             else:
#                 pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)
#                 with st.container(horizontal=True):
#                     if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                         uwp_water_pressure = st.number_input("Tekanan Air Proses UWP", value=None, placeholder="", key="uwp_water_pressure", format="%0.1f", step=0.1)
#                     else:
#                         pass
#                     if df_data_page_1["Mesin"][0] == 'E06':
#                         uwp_water_flow = st.number_input("Flow/Debit Air Proses UWP", value=None, placeholder="", key="uwp_water_flow", format="%d", step=1)
#                     else:
#                         pass
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Jenis Cutter Hub</h5>", unsafe_allow_html=True)
#                 cutter_hub_options = ["E05; Blade 10","E06; Blade 6","E06; Blade 9"]
#                 cutter_hub_options = st.radio('', cutter_hub_options, key="cutter_hub_options")
#         else:
#             pass
        
#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Mesh Screen</h5>", unsafe_allow_html=True)
#             mesh_screen_options = ["SUS 403; 20 mesh","SUS 403; 40 mesh","SUS 403; 60 mesh","SUS 403; 80 mesh","SUS 403; 100 mesh",
#             "SUS 403; 120 mesh","SUS 403; 250 mesh","Dutch Weave; 80 mesh","Dutch Weave; 100 mesh","Dutch Weave; 250 mesh"]
#             mesh_screen_options = st.radio('', mesh_screen_options, key="mesh_screen_options")

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     temperature_in_proses = st.number_input("Temperature In Air Proses", value=None, placeholder="", key="temperature_in_proses", format="%d", step=1)
#                     temperature_out_proses = st.number_input("Temperature Out Air Proses", value=None, placeholder="", key="temperature_out_proses", format="%d", step=1)
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>Air Cooling Tower - HE UWP</h5>", unsafe_allow_html=True)

#                 with st.container(horizontal=True):
#                     temperature_in_cooling_water = st.number_input("Temperature In Air Cooling Water", value=None, placeholder="", key="temperature_in_cooling_water", format="%d", step=1)
#                     temperature_out_cooling_water = st.number_input("Temperaure Out Air Cooling Water", value=None, placeholder="", key="temperature_out_cooling_water", format="%d", step=1)
#         else:
#             pass

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>Parameter Produk FG</h5>", unsafe_allow_html=True)

#             with st.container(horizontal=True):
#                 actual_output_finished_good = st.number_input("Output Aktual FG", value=None, placeholder="", key="actual_output_finished_good", format="%d", step=1)
#                 granule_number = st.number_input("Jumlah Granule/Gram", value=None, placeholder="", key="granule_number", format="%d", step=1)

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             with st.container(border=True):
#                 st.markdown(f"<h5 style='text-align: left;'>JUMLAH DIE HOLE TERBUKA</h5>", unsafe_allow_html=True)
#                 die_hole_open_calc = st.number_input("HASIL PERHITUNGAN", key="die_hole_open_calc")
#         else:
#             pass

            
#         can_submit = True

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if foto_uwp is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if set_temperature_adapter is None:
#                 can_submit = False
#             if actual_temperature_adapter is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if set_temperature_podv is None:
#                 can_submit = False
#             if actual_temperature_podv is None:
#                 can_submit = False
#         else:
#             pass

#         if set_temperature_die_plate is None:
#             can_submit = False
#         if actual_temperature_die_plate is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if set_temperature_water_tank is None:
#                 can_submit = False
#             if actual_temperature_water_tank is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if melt_pressure_uwp is None:
#                 can_submit = False
#             if melt_temperature_uwp is None:
#                 can_submit = False
#         else:
#             pass

#         if die_plate_options is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if ampere_cutter is None:
#                 can_submit = False
#         else:
#             pass

#         if rpm_cutter is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if setting_cutter is None:
#                 can_submit = False
#             if percentage_cutter is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if uwp_water_pressure is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06':
#             if uwp_water_flow is None:
#                 can_submit = False
#         else:
#             pass

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if cutter_hub_options is None:
#                 can_submit = False
#         else:
#             pass

#         if mesh_screen_options is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if temperature_in_proses is None:
#                 can_submit = False
#             if temperature_out_proses is None:
#                 can_submit = False
#             if temperature_in_cooling_water is None:
#                 can_submit = False
#             if temperature_out_cooling_water is None:
#                 can_submit = False
#         else:
#             pass

#         if actual_output_finished_good is None:
#             can_submit = False

#         if granule_number is None:
#             can_submit = False

#         if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#             if die_hole_open_calc is None:
#                 can_submit = False
#         else:
#             pass

#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_4_1 = st.form_submit_button(label='Submit', width = "stretch")

#         if submit_button_4_1:

#             if can_submit == False:
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if foto_uwp is None:
#                         st.toast('Ambil Foto Panel UWP !', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if set_temperature_adapter is None:
#                         st.toast('Isi bagian "Set Point Temperature Adapter"!', icon="⚠️")
#                     if actual_temperature_adapter is None:
#                         st.toast('Isi bagian "Aktual Temperature Adapter"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if set_temperature_podv is None:
#                         st.toast('Isi bagian "Set Point Temperature PoDV"!', icon="⚠️")
#                     if actual_temperature_podv is None:
#                         st.toast('Isi bagian "Aktual Temperature PoDV"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if set_temperature_die_plate is None:
#                     st.toast('Isi bagian "Set Point Temperature Die Plate"!', icon="⚠️")
#                 if actual_temperature_die_plate is None:
#                     st.toast('Isi bagian "Aktual Temperature Die Plate"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if set_temperature_water_tank is None:
#                         st.toast('Isi bagian "Set Point Temperature Water Tank"!', icon="⚠️")
#                     if actual_temperature_water_tank is None:
#                         st.toast('Isi bagian "Aktual Temperature Water Tank"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if melt_pressure_uwp is None:
#                         st.toast('Isi bagian "Melt Pressure UWP"!', icon="⚠️")
#                     if melt_temperature_uwp is None:
#                         st.toast('Isi bagian "Melt Temperature UWP"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if die_plate_options is None:
#                     st.toast('Isi bagian "Jenis Die Plate"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if ampere_cutter is None:
#                         st.toast('Isi bagian "Ampere/Torsi Cutter"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if rpm_cutter is None:
#                     st.toast('Isi bagian "RPM Cutter"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if setting_cutter is None:
#                         st.toast('Isi bagian "Setting Maju Cutter"!', icon="⚠️")
#                     if percentage_cutter is None:
#                         st.toast('Isi bagian "% Panjang Cutter"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if uwp_water_pressure is None:
#                         st.toast('Isi bagian "Tekanan Air Proses UWP"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06':
#                     if uwp_water_flow is None:
#                         st.toast('Isi bagian "Flow Air Proses UWP"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if cutter_hub_options is None:
#                         st.toast('Isi bagian "Jenis Cutter Hub"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if mesh_screen_options is None:
#                     st.toast('Isi bagian "Mesh Screen"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if temperature_in_proses is None:
#                         st.toast('Isi bagian "Temperature In Air Proses"!', icon="⚠️")
#                     if temperature_out_proses is None:
#                         st.toast('Isi bagian "Temperature Out Air Proses"!', icon="⚠️")
#                     if temperature_in_cooling_water is None:
#                         st.toast('Isi bagian "Temperature In Air Cooling Tower"!', icon="⚠️")
#                     if temperature_out_cooling_water is None:
#                         st.toast('Isi bagian "Temperature Out Air Cooling Tower"!', icon="⚠️")
#                 else:
#                     pass
        
#                 if actual_output_finished_good is None:
#                     st.toast('Isi bagian "Output Aktual FG"!', icon="⚠️")
        
#                 if granule_number is None:
#                     st.toast('Isi bagian "Jumlah Granule per Gram"!', icon="⚠️")
        
#                 if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
#                     if die_hole_open_calc is None:
#                         st.toast('Isi bagian "Perhitungan Jumlah Die Hole Terbuka"!', icon="⚠️")
#                 else:
#                     pass
                
#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
#             else:
#                 nama_kolom_page_4 = {
#                     "Dokumentasi Panel UWP":[],
#                     "Set Point Temperature Adapter": [], 
#                     "Aktual Temperature Adapter": [], 
#                     "Set Point Temperature PoDV": [], 
#                     "Aktual Temperature PoDV": [], 
#                     "Set Point Temperature Die Plate": [], 
#                     "Aktual Temperature Die Plate": [], 
#                     "Set Point Temperature Water Tank": [], 
#                     "Aktual Temperature Water Tank": [],
#                     "Melt Pressure UWP": [],
#                     "Melt Temperature UWP": [], 
#                     "Ampere/Torsi Cutter": [], 
#                     "RPM Cutter": [],
#                     "Setting Maju Cutter": [], 
#                     "% Panjang Cutter": [],
#                     "Tekanan Air Proses UWP": [], 
#                     "Flow Air Proses UWP": [], 
#                     "Temperature In Air Proses": [], 
#                     "Temperature Out Air Proses": [],
#                     "Temperature In Air Cooling Tower": [], 
#                     "Temperature Out Air Cooling Tower": [],
#                     "Output Aktual FG": [], 
#                     "Jumlah Granule per Gram": [],
#                     "Perhitungan Jumlah Die Hole Terbuka": [], 
#                     }
#                 df_data_page_4 = pd.DataFrame(nama_kolom_page_4)

#                 new_row_page_4 = pd.DataFrame({
#                     # "Dokumentasi Panel UWP": [foto_uwp_base64],
#                     "Dokumentasi Panel UWP": [foto_uwp_path],
#                     "Set Point Temperature Adapter": [set_temperature_adapter], 
#                     "Aktual Temperature Adapter": [actual_temperature_adapter], 
#                     "Set Point Temperature PoDV": [set_temperature_podv], 
#                     "Aktual Temperature PoDV": [actual_temperature_podv], 
#                     "Set Point Temperature Die Plate": [set_temperature_die_plate], 
#                     "Aktual Temperature Die Plate": [actual_temperature_die_plate], 
#                     "Set Point Temperature Water Tank": [set_temperature_water_tank], 
#                     "Aktual Temperature Water Tank": [actual_temperature_water_tank],
#                     "Melt Pressure UWP": [melt_pressure_uwp],
#                     "Melt Temperature UWP": [melt_temperature_uwp], 
#                     "Ampere/Torsi Cutter": [ampere_cutter], 
#                     "RPM Cutter": [rpm_cutter],
#                     "Setting Maju Cutter": [setting_cutter], 
#                     "% Panjang Cutter": [percentage_cutter],
#                     "Tekanan Air Proses UWP": [uwp_water_pressure], 
#                     "Flow Air Proses UWP": [uwp_water_flow], 
#                     "Temperature In Air Proses": [temperature_in_proses], 
#                     "Temperature Out Air Proses": [temperature_out_proses],
#                     "Temperature In Air Cooling Tower": [temperature_in_cooling_water], 
#                     "Temperature Out Air Cooling Tower": [temperature_out_cooling_water],
#                     "Output Aktual FG": [actual_output_finished_good], 
#                     "Jumlah Granule per Gram": [granule_number],
#                     "Perhitungan Jumlah Die Hole Terbuka": [die_hole_open_calc] 
#                 })
#                 df_data_page_4 = pd.concat([df_data_page_4, new_row_page_4]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_4.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_4 = df_data_page_4
    

#     with st.container(horizontal=True):
#         back_button_4 = st.button("◀️ Kembali", width="stretch")
#         submit_button_2_4 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
#     if submit_button_2_4:
#         if "df_data_page_4" not in st.session_state:
#             # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#             # time.sleep(2)
#         else:
#             if foto_uwp is not None:
#                 foto_uwp, path_to_save_uwp, file_name_uwp = save_image(image = foto_uwp, path_to_save = path_to_save_uwp, file_name = file_name_uwp)
#             else:
#                 pass
#             st.session_state.page = 5
#             st.session_state.scroll_to_top = True
#             st.rerun()
            
 
        

#     @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
#     def backpage_4():
#         with st.container(horizontal=True):
#             button_no_4 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_4 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_4:
#                 if 'df_data_page_4' in st.session_state:
#                     del st.session_state['df_data_page_4']
#                 del st.session_state['df_data_page_3']
#                 st.session_state.page = 3
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_4:
#                 st.rerun()

        
#     if back_button_4:
#         backpage_4()

        
        
        

# #Halaman 5
# if st.session_state["page"] == 5:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
     
    
#     df_data_page_1 = st.session_state.df_data_page_1
    
#     if df_data_page_1["Kondisi Mesin"][0] == "Stop":
#         nama_kolom_page_2 = {
#                     "Set Point Output Feeder 1 - F1 (kg/jam)": [None], 
#                     "Aktual Output Feeder 1 - F1 (kg/jam)": [None], 
#                     "Set Point Output Feeder 2 - F2 (kg/jam)": [None], 
#                     "Aktual Output Feeder 2 - F2 (kg/jam)": [None], 
#                     "Set Point Output Feeder 3 - F3 (kg/jam)": [None], 
#                     "Aktual Output Feeder 3 - F3 (kg/jam)": [None], 
#                     "Set Point Output Feeder 4 - F4 (kg/jam)": [None], 
#                     "Aktual Output Feeder 4 - F4 (kg/jam)": [None], 
#                     "Set Point Output Feeder Jotam S50 (kg/jam)": [None], 
#                     "Aktual Output Feeder Jotam S50 (kg/jam)": [None], 
#                     "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [None], 
#                     "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [None], 
#                     "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [None], 
#                     "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [None], 
#                     "Set Point Output Liquid Feeder (kg/jam)": [None], 
#                     "Aktual Output Liquid Feeder (kg/jam)": [None], 
#                     "Tekanan Liquid Feeder": [None], 
#                     "RPM Main Feeder": [None], 
#                     "Ampere Main Feeder": [None], 
#                     "RPM Feeder Rework": [None], 
#                     "RPM Side Feeder": [None] 
#                     }
#         df_data_page_2 = pd.DataFrame(nama_kolom_page_2)
#         st.session_state.df_data_page_2 = df_data_page_2

#         nama_kolom_page_3 = {
#                     "Dokumentasi Panel Mesin Extruder":[None],
#                     "Set Point Output Mesin": [None], 
#                     "Aktual Output Mesin": [None], 
#                     "Set Point Ampere & RPM Extruder": [None], 
#                     "Aktual Ampere & RPM Extruder": [None], 
#                     "SEI": [None], 
#                     "Melt Temperature Extruder": [None], 
#                     "Melt Pressure Extruder": [None], 
#                     "Kondisi Valve Pendingin Barrel Zone 1": [None], 
#                     "Set Point Temperature Zone 1": [None], 
#                     "Aktual Temperature Zone 1": [None],
#                     "Set Point Temperature Zone 2": [None], 
#                     "Aktual Temperature Zone 2": [None],
#                     "Set Point Temperature Zone 3": [None], 
#                     "Aktual Temperature Zone 3": [None], 
#                     "Set Point Temperature Zone 4": [None], 
#                     "Aktual Temperature Zone 4": [None],
#                     "Set Point Temperature Zone 5": [None], 
#                     "Aktual Temperature Zone 5": [None],
#                     "Set Point Temperature Zone 6": [None], 
#                     "Aktual Temperature Zone 6": [None],
#                     "Set Point Temperature Zone 7": [None], 
#                     "Aktual Temperature Zone 7": [None],
#                     "Set Point Temperature Zone 8": [None], 
#                     "Aktual Temperature Zone 8": [None],
#                     "Set Point Temperature Zone 9": [None], 
#                     "Aktual Temperature Zone 9": [None],
#                     "Set Point Temperature Zone 10": [None], 
#                     "Aktual Temperature Zone 10": [None],
#                     "Set Point Temperature Zone 11": [None], 
#                     "Aktual Temperature Zone 11": [None],
#                     "Set Point Temperature Zone 12": [None], 
#                     "Aktual Temperature Zone 12": [None],
#                     "Set Point Temperature 8.0": [None], 
#                     "Aktual Temperature 8.0": [None], 
#                     "Set Point Temperature Input Screen Changer": [None], 
#                     "Aktual Temperature Input Screen Changer": [None], 
#                     "Set Point Temperature TSW / Screen Changer 1": [None], 
#                     "Aktual Temperature TSW / Screen Changer 1": [None], 
#                     "Set Point Temperature Screen Changer 2": [None], 
#                     "Aktual Temperature Screen Changer 2": [None], 
#                     "Temperature Air Cooling Barrel Mesin (Soft Water)": [None],
#                     "Temperature Air Cooling Gearbox (Cooling Water)": [None], 
#                     "Tekanan Air Cooling Barrel Mesin": [None], 
#                     "Temperature Oli Gearbox": [None] ,
#                     "Vacuum Bar": [None],
#                     "Tekanan Air Vacuum System":[None]
#                     }
#         df_data_page_3 = pd.DataFrame(nama_kolom_page_3)
#         st.session_state.df_data_page_3 = df_data_page_3

#         nama_kolom_page_4 = {
#                     "Dokumentasi Panel UWP":[None],
#                     "Set Point Temperature Adapter": [None], 
#                     "Aktual Temperature Adapter": [None], 
#                     "Set Point Temperature PoDV": [None], 
#                     "Aktual Temperature PoDV": [None], 
#                     "Set Point Temperature Die Plate": [None], 
#                     "Aktual Temperature Die Plate": [None], 
#                     "Set Point Temperature Water Tank": [None], 
#                     "Aktual Temperature Water Tank": [None],
#                     "Melt Pressure UWP": [None],
#                     "Melt Temperature UWP": [None], 
#                     "Ampere/Torsi Cutter": [None], 
#                     "RPM Cutter": [None],
#                     "Setting Maju Cutter": [None], 
#                     "% Panjang Cutter": [None],
#                     "Tekanan Air Proses UWP": [None], 
#                     "Flow Air Proses UWP": [None], 
#                     "Temperature In Air Proses": [None], 
#                     "Temperature Out Air Proses": [None],
#                     "Temperature In Air Cooling Tower": [None], 
#                     "Temperature Out Air Cooling Tower": [None],
#                     "Output Aktual FG": [None], 
#                     "Jumlah Granule per Gram": [None],
#                     "Perhitungan Jumlah Die Hole Terbuka": [None], 
#                     }
#         df_data_page_4 = pd.DataFrame(nama_kolom_page_4)
#         st.session_state.df_data_page_4 = df_data_page_4
        


#     st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 6/6 : QUANTITY REWORK</h3>", unsafe_allow_html=True)
#     # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
#     # st.write(df_all_data)

#     with st.form(key='form_page_5', clear_on_submit=False):

#         tailing_rework = None
#         gandeng_rework = None
#         gramasi_rework = None
#         homogen_rework = None
#         phorous_rework = None
#         tailing_rework = None
#         disperse_rework = None

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK TAILING</h5>", unsafe_allow_html=True)
#             tailing_rework = st.number_input("", key="tailing_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GANDENG/DEMPET</h5>", unsafe_allow_html=True)
#             gandeng_rework = st.number_input("", key="gandeng_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HAZY</h5>", unsafe_allow_html=True)
#             hazy_rework = st.number_input("", key="hazy_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK DISPERSE</h5>", unsafe_allow_html=True)
#             disperse_rework = st.number_input("", key="disperse_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GRAMASI</h5>", unsafe_allow_html=True)
#             gramasi_rework = st.number_input("", key="gramasi_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HOMOGEN</h5>", unsafe_allow_html=True)
#             homogen_rework = st.number_input("", key="homogen_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK PHOROUS</h5>", unsafe_allow_html=True)
#             phorous_rework = st.number_input("", key="phorous_rework", format="%d", step=1)

#         with st.container(border=True):
#             st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK REKONDISI</h5>", unsafe_allow_html=True)
#             rekondisi_rework = st.number_input("", key="rekondisi_rework", format="%d", step=1)

#         can_submit = True

#         if tailing_rework is None:
#             can_submit = False
        
#         if gandeng_rework is None:
#             can_submit = False

#         if hazy_rework is None:
#             can_submit = False

#         if disperse_rework is None:
#             can_submit = False

#         if gramasi_rework is None:
#             can_submit = False

#         if homogen_rework is None:
#             can_submit = False

#         if phorous_rework is None:
#             can_submit = False

#         if rekondisi_rework is None:
#             can_submit = False

#         with stylable_container(
#             "dark blue",
#             css_styles="""
#             button {
#                 background-color: #283281 !important;
#                 color: white !important;
#                 border: none !important;
#                 transition: background-color 0.3s ease;
#                 margin-bottom: 20px !important;  /* Add space after button */
#             }""",
#         ):
#             submit_button_5_1 = st.form_submit_button(label='Submit', width = "stretch")

#         if submit_button_5_1:

#             if can_submit == False:
#                 if tailing_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Tailing"!', icon="⚠️")
                
#                 if gandeng_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Gandeng/Dempet"!', icon="⚠️")
        
#                 if hazy_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Hazy"!', icon="⚠️")
        
#                 if disperse_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Disperse"!', icon="⚠️")
        
#                 if gramasi_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Gramasi"!', icon="⚠️")
        
#                 if homogen_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Homogen"!', icon="⚠️")
        
#                 if phorous_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Phorous"!', icon="⚠️")
        
#                 if rekondisi_rework is None:
#                     st.toast('Isi bagian "Quantity Rework Rekondisi"!', icon="⚠️")
                    
#                 st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
#             else:
#                 nama_kolom_page_5 = {
#                     "Quantity Rework Tailing": [], 
#                     "Quantity Rework Gandeng/Dempet": [], 
#                     "Quantity Rework Hazy": [], 
#                     "Quantity Rework Disperse": [], 
#                     "Quantity Rework Gramasi": [], 
#                     "Quantity Rework Homogen": [], 
#                     "Quantity Rework Phorous": [], 
#                     "Quantity Rework Rekondisi": [],  
#                     }
#                 df_data_page_5 = pd.DataFrame(nama_kolom_page_5)

#                 new_row_page_5 = pd.DataFrame({
#                     "Quantity Rework Tailing": [tailing_rework], 
#                     "Quantity Rework Gandeng/Dempet": [gandeng_rework], 
#                     "Quantity Rework Hazy": [hazy_rework], 
#                     "Quantity Rework Disperse": [disperse_rework], 
#                     "Quantity Rework Gramasi": [gramasi_rework], 
#                     "Quantity Rework Homogen": [homogen_rework], 
#                     "Quantity Rework Phorous": [phorous_rework], 
#                     "Quantity Rework Rekondisi": [rekondisi_rework] 
#                 })
#                 df_data_page_5 = pd.concat([df_data_page_5, new_row_page_5]).reset_index(drop=True)
#                 st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
#                 st.write(df_data_page_5.dropna(axis=1, inplace=False))
#                 st.session_state.df_data_page_5 = df_data_page_5
    

#     with st.container(horizontal=True):
#         back_button_5 = st.button("◀️ Kembali", width="stretch")
#         submit_button_2_5 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
#     if submit_button_2_5:
#         if "df_data_page_5" not in st.session_state:
#             # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
#             st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
#             # time.sleep(2)
#         else:
#             st.session_state.page = 6
#             st.session_state.scroll_to_top = True
#             st.rerun()
            

        

#     @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
#     def backpage_5():
#         with st.container(horizontal=True):
#             button_no_5 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_5 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_5:
#                 if 'df_data_page_5' in st.session_state:
#                     del st.session_state['df_data_page_5']
#                 if df_data_page_1["Kondisi Mesin"][0] == 'Running':
#                     del st.session_state['df_data_page_4']
#                     st.session_state.page = 4 
#                 else:
#                     del st.session_state['df_data_page_1']
#                     st.session_state.page = 1
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_5:
#                 st.rerun()
                
#     if back_button_5:
#         backpage_5()
        
        

#     back_button_5_to_1 = st.button("⏪ Kembali ke Halaman 1")

#     @st.dialog("Apakah Anda yakin akan kembali ke halaman awal?")
#     def backpage_5_to_1():
#         with st.container(horizontal=True):
#             button_no_5_to_1 = st.button(label='Tidak', width="stretch", type="secondary")
#             button_yes_5_to_1 = st.button(label='Ya', width="stretch", type="primary")

#             if button_yes_5_to_1:
#                 if 'df_data_page_6' in st.session_state:
#                     del st.session_state['df_data_page_6']
#                 if df_data_page_1["Kondisi Mesin"][0] == 'Running':
#                     del st.session_state['df_data_page_5']
#                     del st.session_state['df_data_page_4']
#                     del st.session_state['df_data_page_3']
#                     del st.session_state['df_data_page_2']
#                     del st.session_state['df_data_page_1_5']
#                     del st.session_state['df_data_page_1']
#                 else :
#                     del st.session_state['df_data_page_1']
#                 st.session_state.page = 1
#                 st.session_state.scroll_to_top = True
#                 st.rerun()

#             if button_no_5_to_1:
#                 st.rerun()
                
#     if back_button_5_to_1:
#         backpage_5_to_1()
    
        
        

# #Halaman 6
# if st.session_state["page"] == 6:
#     if st.session_state.get("scroll_to_top", False):
#         scroll_to_top()
#         st.session_state.scroll_to_top = False
     
    
#     df_data_page_1 = st.session_state.df_data_page_1
#     df_data_page_2 = st.session_state.df_data_page_2
#     df_data_page_3 = st.session_state.df_data_page_3
#     df_data_page_4 = st.session_state.df_data_page_4
#     df_data_page_5 = st.session_state.df_data_page_5
#     submit_time_now = datetime.now()
#     submit_time = pd.DataFrame({
#                     "Submit Time": [submit_time_now]
#                 })

#     all_df_new_row = pd.concat([df_data_page_1, df_data_page_2, df_data_page_3, df_data_page_4, df_data_page_5, submit_time], axis=1)

#     new_df = save_data(all_df_new_row)

#     st.markdown(
#         """
#         <h2 style='text-align: center; color: green;'>
#             ✅ Terima Kasih!
#         </h2>
#         <h4 style='text-align: center;'>
#             Terima kasih telah mengisi <b>e-Monitoring Produksi</b>.
#         </h4>
#         <p style='text-align: center;'>
#             Data yang Anda masukkan sudah tersimpan dengan baik.
#         </p>
#         """,
#         unsafe_allow_html=True
#     )










# IMPORT LIBRARY
import streamlit as st
import pandas as pd
import numpy as np
import os
import xlsxwriter
# import base64
from datetime import datetime
import cv2
from PIL import Image
from io import BytesIO
import time
from streamlit_extras.stylable_container import stylable_container


def collect_image(nama_layar):
    datetime_now = datetime.now()
    date_number = datetime_now.strftime('%Y-%m-%d')
    time = datetime_now.strftime('%H')+'-'+datetime_now.strftime('%M')+'-'+datetime_now.strftime('%S')
    file_name = str(nama_layar) + ' - ' + str(date_number) + ' ' + str(time) + '.jpg'
    path_to_save = os.path.join(os.getcwd(), 'saved_image')

    if not os.path.exists(path_to_save):
        os.makedirs(path_to_save)

    return path_to_save, file_name

def save_image(image, path_to_save, file_name):

    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    result_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(result_img)
    img_pil.save(os.path.join(path_to_save, file_name), "JPEG")

    return img_pil, path_to_save, file_name

def save_data(df):
    path_to_save_data = os.path.join(os.getcwd(), 'output_data_emonitoring')

    if not os.path.exists(path_to_save_data):
        os.makedirs(path_to_save_data)
        new_df = df.copy()
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer: 
            new_df = new_df.to_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name="Sheet1", startrow=0, header=True, index=False)
    
    else:
        df_exist = pd.read_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name='Sheet1', parse_dates=False)
        new_df = pd.concat([df_exist, df])

        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer: 
            new_df = new_df.to_excel(os.path.join(path_to_save_data, 'data_monitoring.xlsx'), sheet_name="Sheet1", startrow=0, header=True, index=False)

    return new_df



def scroll_to_top():
    scroll_js = """
        <script>
        const main = window.parent.document.querySelector('section.main');
        if (main) {
            main.scrollTo({ top: 0, behavior: 'smooth' });
        }
        </script>
    """
    container = st.empty()
    container.markdown(scroll_js, unsafe_allow_html=True)
    time.sleep(0.5)
    container.empty()
    


st.cache_data.clear()
if "initialized" not in st.session_state:
    st.session_state.clear()  # Clears everything
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.initialized = True  # Set a flag to prevent repeated clearing




logo = Image.open('assets_logo/Logo Dunia Kimia Jaya.png')

st.logo(logo, size="large")

footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #edf2fa;
color: black;
text-align: left;
}
</style>
<div class="footer">
<p style="margin-left: 15px">e-monitoring produksi DKJ ver 1.0 </p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

# Halaman Awal

if "page" not in st.session_state:
    st.session_state["page"] = 0

if st.session_state["page"] == 0 :
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
    
    col_00, col_01, col_02 = st.columns([1, 3, 1])
    with col_01:
        st.image(logo)
    
    st.markdown(f"<h2 style='text-align: center;'>WELCOME TO E-MONITORING PRODUKSI<br>DUNIA KIMIA JAYA</h2>", unsafe_allow_html=True)
    st.markdown("""---""")
    
    left_0, middle_0, right_0 = st.columns(3)
    with middle_0:
        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            tombol_mulai = st.button(type="primary", label='Mulai', width="stretch")
    if tombol_mulai:
        st.session_state.page = 1
        st.session_state.scroll_to_top = True
        st.rerun()
        
        

# Halaman 1
if st.session_state["page"] == 1:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False

     
    
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 1/6 : DATA UMUM</h3>", unsafe_allow_html=True)

    with st.form(key='form_page_1', clear_on_submit=False):
        nama_operator = st.text_input("Nama Operator", key="nama_operator")
        
        with st.container(horizontal=True):
            machine_options = ["Lab","E01", "E02", "E03", "E05", "E06"]
            machine_selected_options = st.radio('Mesin', machine_options, key="machine_selected_options")
            
            shift_options = ["1", "2", "3"]
            shift_selected_options = st.radio('Shift', shift_options, key="shift_selected_options")
            
            group_options = ["Kuning", "Hijau", "Merah", "Biru"]
            group_selected_options = st.radio('Grup', group_options, key="group_selected_options")
            
        with st.container(horizontal=True):
            date_input = st.date_input("Tanggal Pengisian")
            time_input = st.time_input("Jam Pengisian",step=3600)
            
        nama_produk = st.text_input("Nama Produk", key="nama_produk")
        # (Tuliskan angka belakang dan huruf lengkap dibelakang angka saja, CONTOH : Untuk produk ASITHYLEN P White 9440 A, cukup tuliskan : 9440 A)
        
        kondisi_mesin_options = ["Running", "Stop"]
        kondisi_mesin_selected_options = st.pills('Kondisi Mesin', options=kondisi_mesin_options, key="kondisi_mesin_selected_options")

        can_submit = True

        if not nama_operator:
            can_submit = False
        if not machine_selected_options:
            can_submit = False
        if not shift_selected_options:
            can_submit = False
        if not group_selected_options:
            can_submit = False
        if not date_input:
            can_submit = False
        if not time_input:
            can_submit = False
        if not nama_produk:
            can_submit = False
        if not kondisi_mesin_selected_options:
            can_submit = False

        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_1_1 = st.form_submit_button(label='Submit', width = "stretch")
                
        if submit_button_1_1:
            if can_submit == False:
                if not nama_operator:
                    st.toast('Isi bagian "Nama Operator"!', icon="⚠️")
                if not machine_selected_options:
                    st.toast('Isi bagian "Mesin"!', icon="⚠️")
                if not shift_selected_options:
                    st.toast('Isi bagian "Shift"!', icon="⚠️")
                if not group_selected_options:
                    st.toast('Isi bagian "Grup"!', icon="⚠️")
                if not date_input:
                    st.toast('Isi bagian "Tanggal Pengisian"!', icon="⚠️")
                if not time_input:
                    st.toast('Isi bagian "Jam Pengisian"!', icon="⚠️")
                if not nama_produk:
                    st.toast('Isi bagian "Nama Produk"!', icon="⚠️")
                if not kondisi_mesin_selected_options:
                    st.toast('Isi bagian "Kondisi Mesin"!', icon="⚠️")

                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")   
                
            else:
                nama_kolom_page_1 = {
                    "Nama Operator": [], 
                    "Mesin": [], 
                    "Shift": [], 
                    "Tanggal Pengisian": [], 
                    "Jam Pengisian": [],
                    "Nama Produk": [],
                    "Kondisi Mesin": []
                    }
                df_data_page_1 = pd.DataFrame(nama_kolom_page_1)
                new_row_page_1 = pd.DataFrame(
                {"Nama Operator": [nama_operator],
                "Mesin": [machine_selected_options],
                "Shift": [shift_selected_options],
                "Tanggal Pengisian": [date_input],
                "Jam Pengisian": [time_input],
                "Nama Produk": [nama_produk],
                "Kondisi Mesin": [kondisi_mesin_selected_options]
                })
                df_data_page_1 = pd.concat([df_data_page_1, new_row_page_1]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_1.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_1 = df_data_page_1


    left_1, middle_1, right_1 = st.columns([1,3,1])
    with right_1:
        submit_button_1_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
                
    if submit_button_1_2:
        if "df_data_page_1" not in st.session_state:
            # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
        else:
            if st.session_state.df_data_page_1["Kondisi Mesin"][0] == "Stop":
                st.session_state.page = 5   # langsung lompat ke halaman 5
            else:
                st.session_state.page = 1.5   # kalau Running, lanjut normal ke halaman 2
            st.session_state.scroll_to_top = True
            st.rerun()
        

        

# Halaman 1.5 - Pilih Feeder
if st.session_state["page"] == 1.5:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
     
       
    st.markdown("<h3 style='text-align: left;'><br>HALAMAN 2/6 : PILIH FEEDER YANG DIGUNAKAN</h3>", unsafe_allow_html=True)

    with st.form(key='form_page_1_5', clear_on_submit=False):

        feeder_options = [
            "Feeder 1 - F1",
            "Feeder 2 - F2",
            "Feeder 3 - F3",
            "Feeder 4 - F4",
            "Feeder Jotam S50",
            "Feeder Jotam S90 Resin",
            "Feeder Jotam S90 Aditif",
            "Liquid Feeder",
            "Main Feeder",
            "Side Feeder",
            "Feeder Rework"
        ]

        selected_feeders = st.multiselect(
            "Pilih feeder yang digunakan:",
            feeder_options,
            key="selected_feeders"
        )

        can_submit = True

        if not selected_feeders:
            can_submit = False

        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_1_1_5 = st.form_submit_button(label='Submit', width = "stretch")
        if submit_button_1_1_5:
            if can_submit == False:
                if not selected_feeders:
                    st.toast('Isi bagian "Feeder yang digunakan"!', icon="⚠️")
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")                
            else:
                nama_kolom_page_1_5 = {
                    "Feeder yang digunakan": []
                    }
                df_data_page_1_5 = pd.DataFrame(nama_kolom_page_1_5)
                new_row_page_1_5 = pd.DataFrame(
                {"Feeder yang digunakan": [selected_feeders]
                })
                df_data_page_1_5 = pd.concat([df_data_page_1_5, new_row_page_1_5]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_1_5.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_1_5 = df_data_page_1_5



    with st.container(horizontal=True):
        back_button_1_5 = st.button("◀️ Kembali", width="stretch")
        submit_button_1_2_5 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
        
    if submit_button_1_2_5:
        if "df_data_page_1_5" not in st.session_state:
            # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
            # time.sleep(2)
        else:
            st.session_state.page = 2   # kalau Running, lanjut normal ke halaman 2
            st.session_state.scroll_to_top = True
            st.rerun()


    
    
        
    @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
    def backpage_1_5():
        with st.container(horizontal=True):
            button_no_1_5 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_1_5 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_1_5:
                if 'df_data_page_1_5' in st.session_state:
                    del st.session_state['df_data_page_1_5']
                del st.session_state['df_data_page_1']
                st.session_state.page = 1
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_1_5:
                st.rerun()

        
    if back_button_1_5:
        backpage_1_5()
        
            


#Halaman 2
if st.session_state["page"] == 2:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False

     
    
    df_data_page_1 = st.session_state.df_data_page_1
    df_data_page_1_5 = st.session_state.df_data_page_1_5
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 3/6 : MESIN FEEDER</h3>", unsafe_allow_html=True)


    with st.form(key='form_page_2', clear_on_submit=False):
        #Inisialisasi semua parameter sebelum proses pengondisian menggunakan fungsi IF
        set_output_feeder_1 = None
        actual_output_feeder_1 = None
        set_output_feeder_2 = None
        actual_output_feeder_2 = None
        set_output_feeder_3 = None
        actual_output_feeder_3 = None
        set_output_feeder_4 = None
        actual_output_feeder_4 = None
        set_output_feeder_jotam_s50 = None
        actual_output_feeder_jotam_s50 = None
        set_output_feeder_jotam_s90_resin = None
        actual_output_feeder_jotam_s90_resin = None
        set_output_feeder_jotam_s90_aditif = None
        actual_output_feeder_jotam_s90_aditif = None
        set_output_liquid_feeder = None
        actual_output_liquid_feeder = None
        tekanan_liquid_feeder = None
        ampere_main_feeder = None
        rpm_main_feeder = None
        rpm_side_feeder = None
        rpm_feeder_rework = None
        
        
        if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder 1 - F1 (kg/jam)</h5>", unsafe_allow_html=True)
                
                with st.container(horizontal=True):
                    set_output_feeder_1 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_1", format="%d", step=1)
                    actual_output_feeder_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_1", format="%d", step=1)
        else:
            set_output_feeder_1 = None
            actual_output_feeder_1 = None
        
    
        
    
        if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]: 
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder 2 - F2 (kg/jam)</h5>", unsafe_allow_html=True)
                
                with st.container(horizontal=True):
                    set_output_feeder_2 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_2", format="%d", step=1)
                    actual_output_feeder_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_2", format="%d", step=1)
        else:
            pass
    
        if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]: 
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder 3 - F3 (kg/jam)</h5>", unsafe_allow_html=True)
                
                with st.container(horizontal=True):
                    set_output_feeder_3 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_3", format="%d", step=1)
                    actual_output_feeder_3 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_3", format="%d", step=1)
        else:
            pass
    
        if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder 4 - F4 (kg/jam)</h5>", unsafe_allow_html=True)
                
                with st.container(horizontal=True):
                    set_output_feeder_4 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_4", format="%d", step=1)
                    actual_output_feeder_4 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_4", format="%d", step=1)
        else :
            pass
    
        if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S50 (kg/jam)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_output_feeder_jotam_s50 = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s50", format="%d", step=1)
                    actual_output_feeder_jotam_s50 = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s50", format="%d", step=1)
        else :
            pass
    
        if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Resin (kg/jam)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_output_feeder_jotam_s90_resin = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s90_resin", format="%d", step=1)
                    actual_output_feeder_jotam_s90_resin = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s90_resin", format="%d", step=1)
        else :
            pass
    
        if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Feeder Jotam S90 - Aditif (kg/jam)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_output_feeder_jotam_s90_aditif = st.number_input("Set Point", value=None, placeholder="", key="set_output_feeder_jotam_s90_aditif", format="%d", step=1)
                    actual_output_feeder_jotam_s90_aditif = st.number_input("Aktual", value=None, placeholder="", key="actual_output_feeder_jotam_s90_aditif", format="%d", step=1)
        else :
            pass
    
        if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Liquid Feeder (kg/jam)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_output_liquid_feeder = st.number_input("Set Point", value=None, placeholder="", key="set_output_liquid_feeder", format="%d", step=1)
                    actual_output_liquid_feeder = st.number_input("Aktual", value=None, placeholder="", key="actual_output_liquid_feeder", format="%d", step=1)
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Tekanan Liquid Feeder</h5>", unsafe_allow_html=True)
                tekanan_liquid_feeder = st.number_input("Tekanan Liquid Feeder", value=None, placeholder="", key="tekanan_liquid_feeder", format="%d", step=1)
        else :
            pass
    
        if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Main Feeder / Feeder 1</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                        rpm_main_feeder = st.number_input("RPM main feeder", value=None, placeholder="", key="rpm_main_feeder", format="%d", step=1)
                    else :
                        pass
                    if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
                        ampere_main_feeder = st.number_input("Ampere main feeder", value=None, placeholder="", key="ampere_main_feeder", format="%0.1f", step=0.1)
                    else :
                        pass
        else:
            pass
    
        if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Feeder Rework</h5>", unsafe_allow_html=True)
                rpm_feeder_rework = st.number_input("RPM feeder rework", value=None, placeholder="", key="rpm_feeder_rework", format="%d", step=1)
        else :
            pass
    
        if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Side Feeder</h5>", unsafe_allow_html=True)
                rpm_side_feeder = st.number_input("RPM side feeder", value=None, placeholder="", key="rpm_side_feeder", format="%d", step=1)
        else :
            pass
        
        can_submit = True
        
        if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_1 is None:
                can_submit = False
            if actual_output_feeder_1 is None:
                can_submit = False
        else:
            pass
    
        if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_2 is None:
                can_submit = False
            if actual_output_feeder_2 is None:
                can_submit = False
        else:
            pass
    
        if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_3 is None:
                can_submit = False
            if actual_output_feeder_3 is None:
                can_submit = False
        else:
            pass
    
        if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_4 is None:
                can_submit = False
            if actual_output_feeder_4 is None:
                can_submit = False
        else:
            pass
    
        if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_jotam_s50 is None:
                can_submit = False
            if actual_output_feeder_jotam_s50 is None:
                can_submit = False
        else:
            pass
    
        if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_jotam_s90_resin is None:
                can_submit = False
            if actual_output_feeder_jotam_s90_resin is None:
                can_submit = False
        else:
            pass
    
        if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_feeder_jotam_s90_aditif is None:
                can_submit = False
            if actual_output_feeder_jotam_s90_aditif is None:
                can_submit = False
        else:
            pass
    
        if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if set_output_liquid_feeder is None:
                can_submit = False
            if actual_output_liquid_feeder is None:
                can_submit = False
            if tekanan_liquid_feeder is None:
                can_submit = False
        else :
            pass
    
        if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                if rpm_main_feeder is None:
                    can_submit = False
            if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
                if ampere_main_feeder is None:
                    can_submit = False

        else :
            pass
    
        if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if rpm_feeder_rework is None:
                can_submit = False
        else :
            pass
    
        if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
            if rpm_side_feeder is None:
                can_submit = False
        else :
            pass

        
        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_2_1 = st.form_submit_button(label='Submit', width = "stretch")
        
    
        if submit_button_2_1:
            if can_submit == False:
                if "Feeder 1 - F1" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_1 is None:
                        st.toast('Isi bagian "Set Point Output Feeder 1 - F1"!', icon="⚠️")
                    if actual_output_feeder_1 is None:
                        st.toast('Isi bagian "Aktual Output Feeder 1 - F1"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder 2 - F2" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_2 is None:
                        st.toast('Isi bagian "Set Point Output Feeder 2 - F2"!', icon="⚠️")
                    if actual_output_feeder_2 is None:
                        st.toast('Isi bagian "Aktual Output Feeder 2 - F2"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder 3 - F3" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_3 is None:
                        st.toast('Isi bagian "Set Point Output Feeder 3 - F3"!', icon="⚠️")
                    if actual_output_feeder_3 is None:
                        st.toast('Isi bagian "Aktual Output Feeder 3 - F3"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder 4 - F4" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_4 is None:
                        st.toast('Isi bagian "Set Point Output Feeder 4 - F4"!', icon="⚠️")
                    if actual_output_feeder_4 is None:
                        st.toast('Isi bagian "Aktual Output Feeder 4 - F4"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder Jotam S50" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_jotam_s50 is None:
                        st.toast('Isi bagian "Set Point Output Feeder Jotam S50"!', icon="⚠️")
                    if actual_output_feeder_jotam_s50 is None:
                        st.toast('Isi bagian "Aktual Output Feeder Jotam S50"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder Jotam S90 Resin" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_jotam_s90_resin is None:
                        st.toast('Isi bagian "Set Point Output Feeder Jotam S90 Resin"!', icon="⚠️")
                    if actual_output_feeder_jotam_s90_resin is None:
                        st.toast('Isi bagian "Aktual Output Feeder Jotam S90 Resin"!', icon="⚠️")
                else:
                    pass
            
                if "Feeder Jotam S90 Aditif" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_feeder_jotam_s90_aditif is None:
                        st.toast('Isi bagian "Set Point Output Feeder Jotam S90 Aditif"!', icon="⚠️")
                    if actual_output_feeder_jotam_s90_aditif is None:
                        st.toast('Isi bagian "Aktual Output Feeder Jotam S90 Aditif"!', icon="⚠️")
                else:
                    pass
            
                if "Liquid Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if set_output_liquid_feeder is None:
                        st.toast('Isi bagian "Set Point Output Liquid Feeder"!', icon="⚠️")
                    if actual_output_liquid_feeder is None:
                        st.toast('Isi bagian "Aktual Output Liquid Feeder"!', icon="⚠️")
                    if tekanan_liquid_feeder is None:
                        st.toast('Isi bagian "Tekanan Liquid Feeder"!', icon="⚠️")
                else :
                    pass
            
                if "Main Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                        if rpm_main_feeder is None:
                            st.toast('Isi bagian "RPM main feeder"!', icon="⚠️")
                    if df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03':
                        if ampere_main_feeder is None:
                            st.toast('Isi bagian "Ampere main feeder"!', icon="⚠️")
                else :
                    pass
            
                if "Feeder Rework" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if rpm_feeder_rework is None:
                        st.toast('Isi bagian "RPM Feeder Rework"!', icon="⚠️")
                else :
                    pass
            
                if "Side Feeder" in df_data_page_1_5["Feeder yang digunakan"].tolist()[0]:
                    if rpm_side_feeder is None:
                        st.toast('Isi bagian "RPM Side Feeder"!', icon="⚠️")
                else :
                    pass
                    
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_2 = {
                    "Set Point Output Feeder 1 - F1 (kg/jam)": [], 
                    "Aktual Output Feeder 1 - F1 (kg/jam)": [], 
                    "Set Point Output Feeder 2 - F2 (kg/jam)": [], 
                    "Aktual Output Feeder 2 - F2 (kg/jam)": [], 
                    "Set Point Output Feeder 3 - F3 (kg/jam)": [], 
                    "Aktual Output Feeder 3 - F3 (kg/jam)": [], 
                    "Set Point Output Feeder 4 - F4 (kg/jam)": [], 
                    "Aktual Output Feeder 4 - F4 (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S50 (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S50 (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [], 
                    "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
                    "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [], 
                    "Set Point Output Liquid Feeder (kg/jam)": [], 
                    "Aktual Output Liquid Feeder (kg/jam)": [], 
                    "Tekanan Liquid Feeder": [], 
                    "RPM Main Feeder": [], 
                    "Ampere Main Feeder": [], 
                    "RPM Feeder Rework": [], 
                    "RPM Side Feeder": [] 
                    }
                df_data_page_2 = pd.DataFrame(nama_kolom_page_2)
    
                new_row_page_2 = pd.DataFrame({
                    "Set Point Output Feeder 1 - F1 (kg/jam)": [set_output_feeder_1], 
                    "Aktual Output Feeder 1 - F1 (kg/jam)": [actual_output_feeder_1], 
                    "Set Point Output Feeder 2 - F2 (kg/jam)": [set_output_feeder_2], 
                    "Aktual Output Feeder 2 - F2 (kg/jam)": [actual_output_feeder_2], 
                    "Set Point Output Feeder 3 - F3 (kg/jam)": [set_output_feeder_3], 
                    "Aktual Output Feeder 3 - F3 (kg/jam)": [actual_output_feeder_3], 
                    "Set Point Output Feeder 4 - F4 (kg/jam)": [set_output_feeder_4], 
                    "Aktual Output Feeder 4 - F4 (kg/jam)": [actual_output_feeder_4], 
                    "Set Point Output Feeder Jotam S50 (kg/jam)": [set_output_feeder_jotam_s50], 
                    "Aktual Output Feeder Jotam S50 (kg/jam)": [actual_output_feeder_jotam_s50], 
                    "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [set_output_feeder_jotam_s90_resin], 
                    "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [actual_output_feeder_jotam_s90_resin], 
                    "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [set_output_feeder_jotam_s90_aditif], 
                    "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [actual_output_feeder_jotam_s90_aditif], 
                    "Set Point Output Liquid Feeder (kg/jam)": [set_output_liquid_feeder], 
                    "Aktual Output Liquid Feeder (kg/jam)": [actual_output_liquid_feeder], 
                    "Tekanan Liquid Feeder": [tekanan_liquid_feeder], 
                    "RPM Main Feeder": [rpm_main_feeder], 
                    "Ampere Main Feeder": [ampere_main_feeder], 
                    "RPM Feeder Rework": [rpm_feeder_rework], 
                    "RPM Side Feeder": [rpm_side_feeder] 
                })
                df_data_page_2 = pd.concat([df_data_page_2, new_row_page_2]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_2.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_2 = df_data_page_2
                

    with st.container(horizontal=True):
        back_button_2 = st.button("◀️ Kembali", width="stretch")
        submit_button_2_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
    if submit_button_2_2:
        if "df_data_page_2" not in st.session_state:
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
        else:
            st.session_state.page = 3
            st.session_state.scroll_to_top = True
            st.rerun()
            
        
        
    @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
    def backpage_2():
        with st.container(horizontal=True):
            button_no_2 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_2 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_2:
                if 'df_data_page_2' in st.session_state:
                    del st.session_state['df_data_page_2']
                del st.session_state['df_data_page_1_5']
                st.session_state.page = 1.5  # kembali ke halaman 1.5
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_2:
                st.rerun()

        
    if back_button_2:
        backpage_2()
        
            
                
        
        

#Halaman 3
if st.session_state["page"] == 3:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
     
    
    df_data_page_1 = st.session_state.df_data_page_1
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 4/6 : EXTRUDER</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
    # st.write(df_all_data)

    with st.form(key='form_page_3', clear_on_submit=False):

        foto_mesin_base64 = None
        set_output_mesin_extruder = None
        actual_output_mesin_extruder = None 
        set_ampere_RPM_extruder = None
        actual_ampere_RPM_extruder = None
        specific_energy_index = None
        set_melt_temperature_extruder = None
        set_melt_pressure_extruder = None
        valve_condition_options = None
        set_temperature_zone_1 = None
        actual_temperature_zone_1 = None
        set_temperature_zone_2 = None
        actual_temperature_zone_2 = None
        set_temperature_zone_3 = None
        actual_temperature_zone_3 = None
        set_temperature_zone_4 = None
        actual_temperature_zone_4 = None
        set_temperature_zone_5 = None
        actual_temperature_zone_5 = None
        set_temperature_zone_6 = None
        actual_temperature_zone_6 = None
        set_temperature_zone_7 = None
        actual_temperature_zone_7 = None
        set_temperature_zone_8 = None
        actual_temperature_zone_8 = None
        set_temperature_zone_9 = None
        actual_temperature_zone_9 = None
        set_temperature_zone_10 = None
        actual_temperature_zone_10 = None
        set_temperature_zone_11 = None
        actual_temperature_zone_11 = None
        set_temperature_zone_12 = None
        actual_temperature_zone_12 = None
        set_temperature_8 = None
        actual_temperature_8 = None
        set_temperature_input_screen_changer = None
        actual_temperature_input_screen_changer = None
        set_temperature_TSW_screen_changer_1 = None
        actual_temperature_TSW_screen_changer_1 = None
        set_temperature_screen_changer_2 = None
        actual_temperature_screen_changer_2 = None
        temperature_cooling_barrel_mesin = None
        temperature_gearbox_cooling = None
        pressure_cooling_barrel_mesin = None
        temperature_gearbox_oil = None
        pressure_gearbox_oil = None
        vacuum_bar_value = None
        pressure_vacuum_system_water = None

        st.markdown(f"<h5 style='text-align: left;'>📷 Dokumentasi Panel Mesin Extruder</h5>", unsafe_allow_html=True)
        foto_mesin = st.camera_input("Ambil foto panel mesin extruder", key="foto_mesin")
        if foto_mesin is not None:
            path_to_save_extruder, file_name_extruder = collect_image(nama_layar = 'extruder')

        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Output Mesin (kg/jam)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_output_mesin_extruder = st.number_input("Set Point", value=None, placeholder="", key="set_output_mesin_extruder", format="%d", step=1)
                    actual_output_mesin_extruder = st.number_input("Aktual", value=None, placeholder="", key="actual_output_mesin_extruder", format="%d", step=1)
        else : 
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Ampere & RPM Extruder</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                set_ampere_RPM_extruder = st.number_input("Ampere/Torsi", value=None, placeholder="", key="set_ampere_RPM_extruder")
                actual_ampere_RPM_extruder = st.number_input("RPM", value=None, placeholder="", key="actual_ampere_RPM_extruder", format="%d", step=1)

        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>SEI (KWh/kg)</h5>", unsafe_allow_html=True)
                specific_energy_index = st.number_input("SEI", key="specific_energy_index", format="%0.2f", step=0.01)
        else :
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Melt Temperature - Pressure Ekstruder</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    set_melt_temperature_extruder = st.number_input("Set Melt Temperature", value=None, placeholder="", key="set_melt_temperature_extruder", format="%d", step=1)
                else : 
                    pass
    
                set_melt_pressure_extruder = st.number_input("Set Melt Pressure", value=None, placeholder="", key="set_melt_pressure_extruder", format="%d", step=1)
   
        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Kondisi Valve Pendingin Barrel Zone 1</h5>", unsafe_allow_html=True)
                valve_condition_options = ["OPEN", "CLOSE"]
                valve_condition_options = st.radio('', valve_condition_options, key="valve_condition_options")
        else :
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 1</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                    set_temperature_zone_1 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_1", format="%d", step=1)
                else :
                    pass

                actual_temperature_zone_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_1", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 2</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                set_temperature_zone_2 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_2", format="%d", step=1)
                actual_temperature_zone_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_2", format="%d", step=1)
        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 3</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                set_temperature_zone_3 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_3", format="%d", step=1)
                actual_temperature_zone_3 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_3", format="%d", step=1)
        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 4</h5>", unsafe_allow_html=True)
            
            with st.container(horizontal=True):
                set_temperature_zone_4 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_4", format="%d", step=1)
                actual_temperature_zone_4 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_4", format="%d", step=1)
                
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 5</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                set_temperature_zone_5 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_5", format="%d", step=1)
                actual_temperature_zone_5 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_5", format="%d", step=1)
        
        if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 6</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_6 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_6", format="%d", step=1)
                    actual_temperature_zone_6 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_6", format="%d", step=1)
            
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 7</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_7 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_7", format="%d", step=1)
                    actual_temperature_zone_7 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_7", format="%d", step=1)
                    
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 8</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_8 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_8", format="%d", step=1)
                    actual_temperature_zone_8 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_8", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 9</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_9 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_9", format="%d", step=1)
                    actual_temperature_zone_9 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_9", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 10</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_10 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_10", format="%d", step=1)
                    actual_temperature_zone_10 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_10", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 11</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_11 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_11", format="%d", step=1)
                    actual_temperature_zone_11 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_11", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E03':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Zone 12</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_zone_12 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_zone_12", format="%d", step=1)
                    actual_temperature_zone_12 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_zone_12", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature 8.0</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_8 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_8", format="%d", step=1)
                    actual_temperature_8 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_8", format="%d", step=1)
        else :
            pass
        
        if df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Input Screen Changer</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_input_screen_changer = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_input_screen_changer", format="%d", step=1)
                    actual_temperature_input_screen_changer = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_input_screen_changer", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature TSW / Screen Changer 1</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_TSW_screen_changer_1 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_TSW_screen_changer_1", format="%d", step=1)
                    actual_temperature_TSW_screen_changer_1 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_TSW_screen_changer_1", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Screen Changer 2</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_screen_changer_2 = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_screen_changer_2", format="%d", step=1)
                    actual_temperature_screen_changer_2 = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_screen_changer_2", format="%d", step=1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Cooling Barrel Mesin (Soft Water)</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    if df_data_page_1["Mesin"][0] == 'E06':
                        temperature_cooling_barrel_mesin = st.number_input("Temperature Air Cooling Barrel", value=None, placeholder="TEMPERATURE", key="temperature_cooling_barrel_mesin", format="%d", step=1)
                    else :
                        pass
    
                    pressure_cooling_barrel_mesin = st.number_input("Tekanan Air Cooling Barrel", value=None, placeholder="TEKANAN AIR", key="pressure_cooling_barrel_mesin", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Cooling Gearbox (Cooling Tower)</h5>", unsafe_allow_html=True)
                temperature_gearbox_cooling = st.number_input("Temperature Cooling Gearbox", value=None, placeholder="", key="temperature_gearbox_cooling", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Parameter Gearbox Mesin</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    temperature_gearbox_oil = st.number_input("Temperature Oli Gearbox", value=None, placeholder="", key="temperature_gearbox_oil", format="%d", step=1)
                    pressure_gearbox_oil = st.number_input("Tekanan Oli Gearbox", value=None, placeholder="", key="pressure_gearbox_oil", format="%0.1f", step=0.1)
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Parameter Vacuum System</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    vacuum_bar_value = st.number_input("Vacuum Bar", value=None, placeholder="", key="vacuum_bar_value", format="%d", step=1)
                    if df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E06':
                        pressure_vacuum_system_water = st.number_input("Tekanan Air Vacuum System", value=None, placeholder="", key="pressure_vacuum_system_water", format="%0.1f", step=0.1)
                    else :
                        pass
        else:
            pass


        
        can_submit = True

        if foto_mesin is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06':
            if set_output_mesin_extruder is None:
                can_submit = False
            if actual_output_mesin_extruder is None:
                can_submit = False
        else : 
            pass

        if set_ampere_RPM_extruder is None:
            can_submit = False
        if actual_ampere_RPM_extruder is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06':
            if specific_energy_index is None:
                can_submit = False
        else : 
            pass

        if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02'or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if set_melt_temperature_extruder is None:
                can_submit = False
        else :
            pass

        if set_melt_pressure_extruder is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06':
            if valve_condition_options is None:
                can_submit = False
        else :
            pass
        
        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
            if set_temperature_zone_1 is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if actual_temperature_zone_1 is None:
                can_submit = False
            if set_temperature_zone_2 is None:
                can_submit = False
            if actual_temperature_zone_2 is None:
                can_submit = False
            if set_temperature_zone_3 is None:
                can_submit = False
            if actual_temperature_zone_3 is None:
                can_submit = False
            if set_temperature_zone_4 is None:
                can_submit = False
            if actual_temperature_zone_4 is None:
                can_submit = False
            if set_temperature_zone_5 is None:
                can_submit = False
            if actual_temperature_zone_5 is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':    
            if set_temperature_zone_6 is None:
                can_submit = False
            if actual_temperature_zone_6 is None:
                can_submit = False
            if set_temperature_zone_7 is None:
                can_submit = False
            if actual_temperature_zone_7 is None:
                can_submit = False
            if set_temperature_zone_8 is None:
                can_submit = False
            if actual_temperature_zone_8 is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if set_temperature_zone_9 is None:
                can_submit = False
            if actual_temperature_zone_9 is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if set_temperature_zone_10 is None:
                can_submit = False
            if actual_temperature_zone_10 is None:
                can_submit = False
        else : 
            pass
        
        if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
            if set_temperature_zone_11 is None:
                can_submit = False
            if actual_temperature_zone_11 is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0]=='E03':
            if set_temperature_zone_12 is None:
                can_submit = False
            if actual_temperature_zone_12 is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0]=='E06':
            if set_temperature_8 is None:
                can_submit = False
            if actual_temperature_8 is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0]=='E05':
            if set_temperature_input_screen_changer is None:
                can_submit = False
            if actual_temperature_input_screen_changer is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0]=='E05' or df_data_page_1["Mesin"][0]=='E06':
            if set_temperature_TSW_screen_changer_1 is None:
                can_submit = False
            if actual_temperature_TSW_screen_changer_1 is None:
                can_submit = False
        else :
            pass
        
        if df_data_page_1["Mesin"][0]=='E05':
            if set_temperature_screen_changer_2 is None:
                can_submit = False
            if actual_temperature_screen_changer_2 is None:
                can_submit = False
        else :
            pass
    
        if df_data_page_1["Mesin"][0]=='E06':
            if temperature_cooling_barrel_mesin is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0]=='E06' or df_data_page_1["Mesin"][0]=='E05':
            if temperature_gearbox_cooling is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if pressure_cooling_barrel_mesin is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0]=='E06':
            if temperature_gearbox_oil is None:
                can_submit = False
            if pressure_gearbox_oil is None:
                can_submit = False
        else :
            pass

        if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
            if vacuum_bar_value is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
            if pressure_vacuum_system_water is None:
                can_submit = False
        else :
            pass

        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_3_1 = st.form_submit_button(label='Submit', width = "stretch")

        if submit_button_3_1:
            if can_submit == False:
                if foto_mesin is None:
                    st.toast('Ambil foto panel extruder', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if set_output_mesin_extruder is None:
                        st.toast('Isi bagian "Set Point Output Mesin"!', icon="⚠️")
                    if actual_output_mesin_extruder is None:
                        st.toast('Isi bagian "Aktual Output Mesin"!', icon="⚠️")
                else : 
                    pass
        
                if set_ampere_RPM_extruder is None:
                    st.toast('Isi bagian "Set Point Ampere & RPM Extruder"!', icon="⚠️")
                if actual_ampere_RPM_extruder is None:
                    st.toast('Isi bagian "Aktual Ampere & RPM Extruder"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if specific_energy_index is None:
                        st.toast('Isi bagian "SEI"!, icon="⚠️"')
                else : 
                    pass
        
                if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E02'or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if set_melt_temperature_extruder is None:
                        st.toast('Isi bagian "Melt Temperature Extruder"!', icon="⚠️")
                else :
                    pass
        
                if set_melt_pressure_extruder is None:
                    st.toast('Isi bagian "Melt Pressure Extruder"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if valve_condition_options is None:
                        st.toast('Isi bagian "Kondisi Valve Pendingin Barrel Zone 1"!', icon="⚠️")
                else :
                    pass
                
                if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05':
                    if set_temperature_zone_1 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 1"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0] == 'Lab' or df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if actual_temperature_zone_1 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 1"!', icon="⚠️")
                    if set_temperature_zone_2 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 2"!', icon="⚠️")
                    if actual_temperature_zone_2 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 2"!', icon="⚠️")
                    if set_temperature_zone_3 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 3"!', icon="⚠️")
                    if actual_temperature_zone_3 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 3"!', icon="⚠️")
                    if set_temperature_zone_4 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 4"!', icon="⚠️")
                    if actual_temperature_zone_4 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 4"!', icon="⚠️")
                    if set_temperature_zone_5 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 5"!', icon="⚠️")
                    if actual_temperature_zone_5 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 5"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':    
                    if set_temperature_zone_6 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 6"!', icon="⚠️")
                    if actual_temperature_zone_6 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 6"!', icon="⚠️")
                    if set_temperature_zone_7 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 7"!', icon="⚠️")
                    if actual_temperature_zone_7 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 7"!', icon="⚠️")
                    if set_temperature_zone_8 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 8"!', icon="⚠️")
                    if actual_temperature_zone_8 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 8"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if set_temperature_zone_9 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 9"!', icon="⚠️")
                    if actual_temperature_zone_9 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 9"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E01'or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if set_temperature_zone_10 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 10"!', icon="⚠️")
                    if actual_temperature_zone_10 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 10"!', icon="⚠️")
                else : 
                    pass
                
                if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
                    if set_temperature_zone_11 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 11"!', icon="⚠️")
                    if actual_temperature_zone_11 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 11"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0]=='E03':
                    if set_temperature_zone_12 is None:
                        st.toast('Isi bagian "Set Point Temperature Zone 12"!', icon="⚠️")
                    if actual_temperature_zone_12 is None:
                        st.toast('Isi bagian "Aktual Temperature Zone 12"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0]=='E06':
                    if set_temperature_8 is None:
                        st.toast('Isi bagian "Set Point Temperature 8.0"!', icon="⚠️")
                    if actual_temperature_8 is None:
                        st.toast('Isi bagian "Aktual Temperature 8.0"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0]=='E05':
                    if set_temperature_input_screen_changer is None:
                        st.toast('Isi bagian "Set Point Temperature Input Screen Changer"!', icon="⚠️")
                    if actual_temperature_input_screen_changer is None:
                        st.toast('Isi bagian "Aktual Temperature Input Screen Changer"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0]=='E05' or df_data_page_1["Mesin"][0]=='E06':
                    if set_temperature_TSW_screen_changer_1 is None:
                        st.toast('Isi bagian "Set Point Temperature TSW / Screen Changer 1"!', icon="⚠️")
                    if actual_temperature_TSW_screen_changer_1 is None:
                        st.toast('Isi bagian "Aktual Temperature TSW / Screen Changer 1"!', icon="⚠️")
                else :
                    pass
                
                if df_data_page_1["Mesin"][0]=='E05':
                    if set_temperature_screen_changer_2 is None:
                        st.toast('Isi bagian "Set Point Temperature Screen Changer 2"!', icon="⚠️")
                    if actual_temperature_screen_changer_2 is None:
                        st.toast('Isi bagian "Aktual Temperature Screen Changer 2"!', icon="⚠️")
                else :
                    pass
            
                if df_data_page_1["Mesin"][0]=='E06':
                    if temperature_cooling_barrel_mesin is None:
                        st.toast('Isi bagian "Temperature Air Cooling Barrel Mesin (Soft Water)"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0]=='E06' or df_data_page_1["Mesin"][0]=='E05':
                    if temperature_gearbox_cooling is None:
                        st.toast('Isi bagian "Temperature Air Cooling Gearbox (Cooling Tower)"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if pressure_cooling_barrel_mesin is None:
                        st.toast('Isi bagian "Tekanan Air Cooling Barrel Mesin"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0]=='E06':
                    if temperature_gearbox_oil is None:
                        st.toast('Isi bagian "Temperature Oli Gearbox"!', icon="⚠️")
                    if pressure_gearbox_oil is None:
                        st.toast('Isi bagian "Tekanan Oli Gearbox"!', icon="⚠️")
                else :
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E01' or df_data_page_1["Mesin"][0] == 'E02' or df_data_page_1["Mesin"][0] == 'E03' or df_data_page_1["Mesin"][0] == 'E05' or df_data_page_1["Mesin"][0] == 'E06':
                    if vacuum_bar_value is None:
                        st.toast('Isi bagian "Vacuum Bar"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0]=='E03' or df_data_page_1["Mesin"][0]=='E06':
                    if pressure_vacuum_system_water is None:
                        st.toast('Isi bagian "Tekanan Air Vacuum System"!', icon="⚠️")
                else :
                    pass
                    
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_3 = {
                    "Dokumentasi Panel Mesin Extruder":[],
                    "Set Point Output Mesin": [], 
                    "Aktual Output Mesin": [], 
                    "Set Point Ampere & RPM Extruder": [], 
                    "Aktual Ampere & RPM Extruder": [], 
                    "SEI": [], 
                    "Melt Temperature Extruder": [], 
                    "Melt Pressure Extruder": [], 
                    "Kondisi Valve Pendingin Barrel Zone 1": [], 
                    "Set Point Temperature Zone 1": [], 
                    "Aktual Temperature Zone 1": [],
                    "Set Point Temperature Zone 2": [], 
                    "Aktual Temperature Zone 2": [],
                    "Set Point Temperature Zone 3": [], 
                    "Aktual Temperature Zone 3": [], 
                    "Set Point Temperature Zone 4": [], 
                    "Aktual Temperature Zone 4": [],
                    "Set Point Temperature Zone 5": [], 
                    "Aktual Temperature Zone 5": [],
                    "Set Point Temperature Zone 6": [], 
                    "Aktual Temperature Zone 6": [],
                    "Set Point Temperature Zone 7": [], 
                    "Aktual Temperature Zone 7": [],
                    "Set Point Temperature Zone 8": [], 
                    "Aktual Temperature Zone 8": [],
                    "Set Point Temperature Zone 9": [], 
                    "Aktual Temperature Zone 9": [],
                    "Set Point Temperature Zone 10": [], 
                    "Aktual Temperature Zone 10": [],
                    "Set Point Temperature Zone 11": [], 
                    "Aktual Temperature Zone 11": [],
                    "Set Point Temperature Zone 12": [], 
                    "Aktual Temperature Zone 12": [],
                    "Set Point Temperature 8.0": [], 
                    "Aktual Temperature 8.0": [], 
                    "Set Point Temperature Input Screen Changer": [], 
                    "Aktual Temperature Input Screen Changer": [], 
                    "Set Point Temperature TSW / Screen Changer 1": [], 
                    "Aktual Temperature TSW / Screen Changer 1": [], 
                    "Set Point Temperature Screen Changer 2": [], 
                    "Aktual Temperature Screen Changer 2": [], 
                    "Temperature Air Cooling Barrel Mesin (Soft Water)": [],
                    "Temperature Air Cooling Gearbox (Cooling Tower)":[], 
                    "Tekanan Air Cooling Barrel Mesin": [], 
                    "Temperature Oli Gearbox": [] ,
                    "Vacuum Bar": [],
                    "Tekanan Air Vacuum System":[]
                    }
                df_data_page_3 = pd.DataFrame(nama_kolom_page_3)

                new_row_page_3 = pd.DataFrame({
                    # "Dokumentasi Panel Mesin Extruder": [foto_mesin_base64],
                    "Dokumentasi Panel Mesin Extruder": [str(os.path.join(path_to_save_extruder, file_name_extruder))],
                    "Set Point Output Mesin": [set_output_mesin_extruder], 
                    "Aktual Output Mesin": [actual_output_mesin_extruder], 
                    "Set Point Ampere & RPM Extruder": [set_ampere_RPM_extruder], 
                    "Aktual Ampere & RPM Extruder": [actual_ampere_RPM_extruder], 
                    "SEI": [specific_energy_index],
                    "Melt Temperature Extruder": [set_melt_temperature_extruder], 
                    "Melt Pressure Extruder": [set_melt_pressure_extruder], 
                    "Kondisi Valve Pendingin Barrel Zone 1": [valve_condition_options], 
                    "Set Point Temperature Zone 1": [set_temperature_zone_1], 
                    "Aktual Temperature Zone 1": [actual_temperature_zone_1],
                    "Set Point Temperature Zone 2": [set_temperature_zone_2], 
                    "Aktual Temperature Zone 2": [actual_temperature_zone_2],
                    "Set Point Temperature Zone 3": [set_temperature_zone_3], 
                    "Aktual Temperature Zone 3": [actual_temperature_zone_3], 
                    "Set Point Temperature Zone 4": [set_temperature_zone_4], 
                    "Aktual Temperature Zone 4": [actual_temperature_zone_4],
                    "Set Point Temperature Zone 5": [set_temperature_zone_5], 
                    "Aktual Temperature Zone 5": [actual_temperature_zone_5],
                    "Set Point Temperature Zone 6": [set_temperature_zone_6], 
                    "Aktual Temperature Zone 6": [actual_temperature_zone_6],
                    "Set Point Temperature Zone 7": [set_temperature_zone_7], 
                    "Aktual Temperature Zone 7": [actual_temperature_zone_7],
                    "Set Point Temperature Zone 8": [set_temperature_zone_8], 
                    "Aktual Temperature Zone 8": [actual_temperature_zone_8],
                    "Set Point Temperature Zone 9": [set_temperature_zone_9], 
                    "Aktual Temperature Zone 9": [actual_temperature_zone_9],
                    "Set Point Temperature Zone 10": [set_temperature_zone_10], 
                    "Aktual Temperature Zone 10": [actual_temperature_zone_10],
                    "Set Point Temperature Zone 11": [set_temperature_zone_11], 
                    "Aktual Temperature Zone 11": [actual_temperature_zone_11],
                    "Set Point Temperature Zone 12": [set_temperature_zone_12], 
                    "Aktual Temperature Zone 12": [actual_temperature_zone_12],
                    "Set Point Temperature 8.0": [set_temperature_8], 
                    "Aktual Temperature 8.0": [actual_temperature_8], 
                    "Set Point Temperature Input Screen Changer": [set_temperature_input_screen_changer], 
                    "Aktual Temperature Input Screen Changer": [actual_temperature_input_screen_changer], 
                    "Set Point Temperature TSW / Screen Changer 1": [set_temperature_TSW_screen_changer_1], 
                    "Aktual Temperature TSW / Screen Changer 1": [actual_temperature_TSW_screen_changer_1], 
                    "Set Point Temperature Screen Changer 2": [set_temperature_screen_changer_2], 
                    "Aktual Temperature Screen Changer 2": [actual_temperature_screen_changer_2], 
                    "Temperature Air Cooling Barrel Mesin (Soft Water)": [temperature_cooling_barrel_mesin], 
                    "Tekanan Air Cooling Barrel Mesin": [pressure_cooling_barrel_mesin],
                    "Temperature Air Cooling Gearbox (Cooling Water)": [temperature_gearbox_cooling], 
                    "Temperature Oli Gearbox": [temperature_gearbox_oil],
                    "Tekanan Oli Gearbox": [pressure_gearbox_oil],
                    "Vacuum Bar": [vacuum_bar_value],
                    "Tekanan Air Vacuum System":[pressure_vacuum_system_water] 
                })
                df_data_page_3 = pd.concat([df_data_page_3, new_row_page_3]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_3.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_3 = df_data_page_3
                
            

    with st.container(horizontal=True) :
        back_button_3 = st.button("◀️ Kembali", width="stretch")
        submit_button_3_2 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
    if submit_button_3_2:
        if "df_data_page_3" not in st.session_state:
            # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
            # time.sleep(2)
        else:
            foto_mesin, path_to_save_extruder, file_name_extruder = save_image(image = foto_mesin, path_to_save = path_to_save_extruder, file_name = file_name_extruder)
            st.session_state.page = 4
            st.session_state.scroll_to_top = True
            st.rerun()
            
        
        
    @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
    def backpage_3():
        with st.container(horizontal=True):
            button_no_3 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_3 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_3:
                if 'df_data_page_3' in st.session_state:
                    del st.session_state['df_data_page_3']
                del st.session_state['df_data_page_2']
                st.session_state.page = 2  # kembali ke halaman 1
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_3:
                st.rerun()

        
    if back_button_3:
        backpage_3()
        
        
        

#Halaman 4
if st.session_state["page"] == 4:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
     
    
    df_data_page_1 = st.session_state.df_data_page_1
    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 5/6 : UWP-PELLETIZER</h3>", unsafe_allow_html=True)


    with st.form(key='form_page_4', clear_on_submit=False):

        set_temperature_adapter = None
        actual_temperature_adapter = None
        set_temperature_podv = None
        actual_temperature_podv = None
        set_temperature_die_plate = None
        actual_temperature_die_plate = None
        set_temperature_water_tank = None
        actual_temperature_water_tank = None
        melt_pressure_uwp = None
        melt_temperature_uwp = None
        die_plate_options = None
        ampere_cutter = None
        rpm_cutter = None
        setting_cutter = None
        percentage_cutter = None
        uwp_water_pressure = None
        uwp_water_flow = None
        cutter_hub_options = None
        mesh_screen_options = None
        temperature_in_proses = None
        temperature_out_proses = None
        temperature_in_cooling_water = None
        temperature_out_cooling_water = None
        actual_output_finished_good = None
        granule_number = None
        die_hole_open_calc = None
        foto_uwp = None
        foto_uwp_path = None

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            st.markdown(f"<h5 style='text-align: left;'>📷 Dokumentasi Panel Underwater Pelletizer</h5>", unsafe_allow_html=True)
            foto_uwp = st.camera_input("Ambil foto panel UWP", key="foto_uwp")
            if foto_uwp is not None:
                path_to_save_uwp, file_name_uwp = collect_image(nama_layar = 'UWP')
                foto_uwp_path = str(os.path.join(path_to_save_uwp, file_name_uwp))

        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Adapter</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_adapter = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_adapter", format="%d", step=1)
                    actual_temperature_adapter = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_adapter", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature PoDV</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_podv = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_podv", format="%d", step=1)
                    actual_temperature_podv = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_podv", format="%d", step=1)
        else:
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Temperature Die Plate</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                set_temperature_die_plate = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_die_plate", format="%d", step=1)
                actual_temperature_die_plate = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_die_plate", format="%d", step=1)

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Temperature Water Tank</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    set_temperature_water_tank = st.number_input("Set Point", value=None, placeholder="", key="set_temperature_water_tank", format="%d", step=1)
                    actual_temperature_water_tank = st.number_input("Aktual", value=None, placeholder="", key="actual_temperature_water_tank", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Melt Parameter pada UWP</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    melt_pressure_uwp = st.number_input("Melt Pressure", value=None, placeholder="", key="melt_pressure_uwp", format="%d", step=1)
                    melt_temperature_uwp = st.number_input("Melt Temperature", value=None, placeholder="", key="melt_temperature_uwp", format="%d", step=1)
        else:
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Jenis Die Plate</h5>", unsafe_allow_html=True)
            die_plate_options = ["Lab; 2 hole","E01; 2.8 mm; 10 hole", "E02; 2 mm; 20 hole","E02; 3.5 mm; 17 hole","E02; 4 mm; 9 hole","E03; 2 mm; 20 hole",
            "E03; 4 mm; 15 hole","E03; 3.5 mm; 7 hole","E05; 2.8 mm; 20 hole","E05; 2.8 mm; 10 hole","E05; 3.2 mm; 10 hole","E06; 2 mm; 48 hole",
            "E06; 2.8 mm; 24 hole"]
            die_plate_options = st.radio('', die_plate_options, key="die_plate_options")

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Cutter</h5>", unsafe_allow_html=True)
            with st.container(horizontal=True):
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    ampere_cutter = st.number_input("Ampere/Torsi Cutter", value=None, placeholder="", key="ampere_cutter", format="%0.1f", step=0.1)
                else:
                    pass
    
                rpm_cutter = st.number_input("RPM Cutter", value=None, placeholder="", key="rpm_cutter", format="%d", step=1)

            
            if df_data_page_1["Mesin"][0] == 'E06':
                with st.container(horizontal=True):
                    setting_cutter = st.number_input("Setting Maju Cutter", value=None, placeholder="", key="setting_cutter", format="%d", step=1)
                    percentage_cutter = st.number_input("% Panjang Cutter", value=None, placeholder="", key="percentage_cutter", format="%d", step=1)
            else:
                pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)
                with st.container(horizontal=True):
                    if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                        uwp_water_pressure = st.number_input("Tekanan Air Proses UWP", value=None, placeholder="", key="uwp_water_pressure", format="%0.1f", step=0.1)
                    else:
                        pass
                    if df_data_page_1["Mesin"][0] == 'E06':
                        uwp_water_flow = st.number_input("Flow/Debit Air Proses UWP", value=None, placeholder="", key="uwp_water_flow", format="%d", step=1)
                    else:
                        pass
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Jenis Cutter Hub</h5>", unsafe_allow_html=True)
                cutter_hub_options = ["E05; Blade 10","E06; Blade 6","E06; Blade 9"]
                cutter_hub_options = st.radio('', cutter_hub_options, key="cutter_hub_options")
        else:
            pass
        
        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Mesh Screen</h5>", unsafe_allow_html=True)
            mesh_screen_options = ["SUS 403; 20 mesh","SUS 403; 40 mesh","SUS 403; 60 mesh","SUS 403; 80 mesh","SUS 403; 100 mesh",
            "SUS 403; 120 mesh","SUS 403; 250 mesh","Dutch Weave; 80 mesh","Dutch Weave; 100 mesh","Dutch Weave; 250 mesh"]
            mesh_screen_options = st.radio('', mesh_screen_options, key="mesh_screen_options")

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Air Proses UWP</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    temperature_in_proses = st.number_input("Temperature In Air Proses", value=None, placeholder="", key="temperature_in_proses", format="%d", step=1)
                    temperature_out_proses = st.number_input("Temperature Out Air Proses", value=None, placeholder="", key="temperature_out_proses", format="%d", step=1)
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>Air Cooling Tower - HE UWP</h5>", unsafe_allow_html=True)

                with st.container(horizontal=True):
                    temperature_in_cooling_water = st.number_input("Temperature In Air Cooling Water", value=None, placeholder="", key="temperature_in_cooling_water", format="%d", step=1)
                    temperature_out_cooling_water = st.number_input("Temperaure Out Air Cooling Water", value=None, placeholder="", key="temperature_out_cooling_water", format="%d", step=1)
        else:
            pass

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>Parameter Produk FG</h5>", unsafe_allow_html=True)

            with st.container(horizontal=True):
                actual_output_finished_good = st.number_input("Output Aktual FG", value=None, placeholder="", key="actual_output_finished_good", format="%d", step=1)
                granule_number = st.number_input("Jumlah Granule/Gram", value=None, placeholder="", key="granule_number", format="%d", step=1)

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            with st.container(border=True):
                st.markdown(f"<h5 style='text-align: left;'>JUMLAH DIE HOLE TERBUKA</h5>", unsafe_allow_html=True)
                die_hole_open_calc = st.number_input("HASIL PERHITUNGAN", key="die_hole_open_calc")
        else:
            pass

            
        can_submit = True

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if foto_uwp is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06':
            if set_temperature_adapter is None:
                can_submit = False
            if actual_temperature_adapter is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if set_temperature_podv is None:
                can_submit = False
            if actual_temperature_podv is None:
                can_submit = False
        else:
            pass

        if set_temperature_die_plate is None:
            can_submit = False
        if actual_temperature_die_plate is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if set_temperature_water_tank is None:
                can_submit = False
            if actual_temperature_water_tank is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if melt_pressure_uwp is None:
                can_submit = False
            if melt_temperature_uwp is None:
                can_submit = False
        else:
            pass

        if die_plate_options is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if ampere_cutter is None:
                can_submit = False
        else:
            pass

        if rpm_cutter is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06':
            if setting_cutter is None:
                can_submit = False
            if percentage_cutter is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if uwp_water_pressure is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06':
            if uwp_water_flow is None:
                can_submit = False
        else:
            pass

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if cutter_hub_options is None:
                can_submit = False
        else:
            pass

        if mesh_screen_options is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if temperature_in_proses is None:
                can_submit = False
            if temperature_out_proses is None:
                can_submit = False
            if temperature_in_cooling_water is None:
                can_submit = False
            if temperature_out_cooling_water is None:
                can_submit = False
        else:
            pass

        if actual_output_finished_good is None:
            can_submit = False

        if granule_number is None:
            can_submit = False

        if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
            if die_hole_open_calc is None:
                can_submit = False
        else:
            pass

        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_4_1 = st.form_submit_button(label='Submit', width = "stretch")

        if submit_button_4_1:

            if can_submit == False:
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if foto_uwp is None:
                        st.toast('Ambil Foto Panel UWP !', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if set_temperature_adapter is None:
                        st.toast('Isi bagian "Set Point Temperature Adapter"!', icon="⚠️")
                    if actual_temperature_adapter is None:
                        st.toast('Isi bagian "Aktual Temperature Adapter"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if set_temperature_podv is None:
                        st.toast('Isi bagian "Set Point Temperature PoDV"!', icon="⚠️")
                    if actual_temperature_podv is None:
                        st.toast('Isi bagian "Aktual Temperature PoDV"!', icon="⚠️")
                else:
                    pass
        
                if set_temperature_die_plate is None:
                    st.toast('Isi bagian "Set Point Temperature Die Plate"!', icon="⚠️")
                if actual_temperature_die_plate is None:
                    st.toast('Isi bagian "Aktual Temperature Die Plate"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if set_temperature_water_tank is None:
                        st.toast('Isi bagian "Set Point Temperature Water Tank"!', icon="⚠️")
                    if actual_temperature_water_tank is None:
                        st.toast('Isi bagian "Aktual Temperature Water Tank"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if melt_pressure_uwp is None:
                        st.toast('Isi bagian "Melt Pressure UWP"!', icon="⚠️")
                    if melt_temperature_uwp is None:
                        st.toast('Isi bagian "Melt Temperature UWP"!', icon="⚠️")
                else:
                    pass
        
                if die_plate_options is None:
                    st.toast('Isi bagian "Jenis Die Plate"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if ampere_cutter is None:
                        st.toast('Isi bagian "Ampere/Torsi Cutter"!', icon="⚠️")
                else:
                    pass
        
                if rpm_cutter is None:
                    st.toast('Isi bagian "RPM Cutter"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if setting_cutter is None:
                        st.toast('Isi bagian "Setting Maju Cutter"!', icon="⚠️")
                    if percentage_cutter is None:
                        st.toast('Isi bagian "% Panjang Cutter"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if uwp_water_pressure is None:
                        st.toast('Isi bagian "Tekanan Air Proses UWP"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06':
                    if uwp_water_flow is None:
                        st.toast('Isi bagian "Flow Air Proses UWP"!', icon="⚠️")
                else:
                    pass
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if cutter_hub_options is None:
                        st.toast('Isi bagian "Jenis Cutter Hub"!', icon="⚠️")
                else:
                    pass
        
                if mesh_screen_options is None:
                    st.toast('Isi bagian "Mesh Screen"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if temperature_in_proses is None:
                        st.toast('Isi bagian "Temperature In Air Proses"!', icon="⚠️")
                    if temperature_out_proses is None:
                        st.toast('Isi bagian "Temperature Out Air Proses"!', icon="⚠️")
                    if temperature_in_cooling_water is None:
                        st.toast('Isi bagian "Temperature In Air Cooling Tower"!', icon="⚠️")
                    if temperature_out_cooling_water is None:
                        st.toast('Isi bagian "Temperature Out Air Cooling Tower"!', icon="⚠️")
                else:
                    pass
        
                if actual_output_finished_good is None:
                    st.toast('Isi bagian "Output Aktual FG"!', icon="⚠️")
        
                if granule_number is None:
                    st.toast('Isi bagian "Jumlah Granule per Gram"!', icon="⚠️")
        
                if df_data_page_1["Mesin"][0] == 'E06' or df_data_page_1["Mesin"][0] == 'E05':
                    if die_hole_open_calc is None:
                        st.toast('Isi bagian "Perhitungan Jumlah Die Hole Terbuka"!', icon="⚠️")
                else:
                    pass
                
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_4 = {
                    "Dokumentasi Panel UWP":[],
                    "Set Point Temperature Adapter": [], 
                    "Aktual Temperature Adapter": [], 
                    "Set Point Temperature PoDV": [], 
                    "Aktual Temperature PoDV": [], 
                    "Set Point Temperature Die Plate": [], 
                    "Aktual Temperature Die Plate": [], 
                    "Set Point Temperature Water Tank": [], 
                    "Aktual Temperature Water Tank": [],
                    "Melt Pressure UWP": [],
                    "Melt Temperature UWP": [], 
                    "Ampere/Torsi Cutter": [], 
                    "RPM Cutter": [],
                    "Setting Maju Cutter": [], 
                    "% Panjang Cutter": [],
                    "Tekanan Air Proses UWP": [], 
                    "Flow Air Proses UWP": [], 
                    "Temperature In Air Proses": [], 
                    "Temperature Out Air Proses": [],
                    "Temperature In Air Cooling Tower": [], 
                    "Temperature Out Air Cooling Tower": [],
                    "Output Aktual FG": [], 
                    "Jumlah Granule per Gram": [],
                    "Perhitungan Jumlah Die Hole Terbuka": [], 
                    }
                df_data_page_4 = pd.DataFrame(nama_kolom_page_4)

                new_row_page_4 = pd.DataFrame({
                    # "Dokumentasi Panel UWP": [foto_uwp_base64],
                    "Dokumentasi Panel UWP": [foto_uwp_path],
                    "Set Point Temperature Adapter": [set_temperature_adapter], 
                    "Aktual Temperature Adapter": [actual_temperature_adapter], 
                    "Set Point Temperature PoDV": [set_temperature_podv], 
                    "Aktual Temperature PoDV": [actual_temperature_podv], 
                    "Set Point Temperature Die Plate": [set_temperature_die_plate], 
                    "Aktual Temperature Die Plate": [actual_temperature_die_plate], 
                    "Set Point Temperature Water Tank": [set_temperature_water_tank], 
                    "Aktual Temperature Water Tank": [actual_temperature_water_tank],
                    "Melt Pressure UWP": [melt_pressure_uwp],
                    "Melt Temperature UWP": [melt_temperature_uwp], 
                    "Ampere/Torsi Cutter": [ampere_cutter], 
                    "RPM Cutter": [rpm_cutter],
                    "Setting Maju Cutter": [setting_cutter], 
                    "% Panjang Cutter": [percentage_cutter],
                    "Tekanan Air Proses UWP": [uwp_water_pressure], 
                    "Flow Air Proses UWP": [uwp_water_flow], 
                    "Temperature In Air Proses": [temperature_in_proses], 
                    "Temperature Out Air Proses": [temperature_out_proses],
                    "Temperature In Air Cooling Tower": [temperature_in_cooling_water], 
                    "Temperature Out Air Cooling Tower": [temperature_out_cooling_water],
                    "Output Aktual FG": [actual_output_finished_good], 
                    "Jumlah Granule per Gram": [granule_number],
                    "Perhitungan Jumlah Die Hole Terbuka": [die_hole_open_calc] 
                })
                df_data_page_4 = pd.concat([df_data_page_4, new_row_page_4]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_4.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_4 = df_data_page_4
    

    with st.container(horizontal=True):
        back_button_4 = st.button("◀️ Kembali", width="stretch")
        submit_button_2_4 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
    if submit_button_2_4:
        if "df_data_page_4" not in st.session_state:
            # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit"sebelum menekan tombol "Next Page"!')
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
            # time.sleep(2)
        else:
            if foto_uwp is not None:
                foto_uwp, path_to_save_uwp, file_name_uwp = save_image(image = foto_uwp, path_to_save = path_to_save_uwp, file_name = file_name_uwp)
            else:
                pass
            st.session_state.page = 5
            st.session_state.scroll_to_top = True
            st.rerun()
            
 
        

    @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
    def backpage_4():
        with st.container(horizontal=True):
            button_no_4 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_4 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_4:
                if 'df_data_page_4' in st.session_state:
                    del st.session_state['df_data_page_4']
                del st.session_state['df_data_page_3']
                st.session_state.page = 3
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_4:
                st.rerun()

        
    if back_button_4:
        backpage_4()

        
        
        

#Halaman 5
if st.session_state["page"] == 5:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
     
    
    df_data_page_1 = st.session_state.df_data_page_1
    
    if df_data_page_1["Kondisi Mesin"][0] == "Stop":
        nama_kolom_page_2 = {
                    "Set Point Output Feeder 1 - F1 (kg/jam)": [None], 
                    "Aktual Output Feeder 1 - F1 (kg/jam)": [None], 
                    "Set Point Output Feeder 2 - F2 (kg/jam)": [None], 
                    "Aktual Output Feeder 2 - F2 (kg/jam)": [None], 
                    "Set Point Output Feeder 3 - F3 (kg/jam)": [None], 
                    "Aktual Output Feeder 3 - F3 (kg/jam)": [None], 
                    "Set Point Output Feeder 4 - F4 (kg/jam)": [None], 
                    "Aktual Output Feeder 4 - F4 (kg/jam)": [None], 
                    "Set Point Output Feeder Jotam S50 (kg/jam)": [None], 
                    "Aktual Output Feeder Jotam S50 (kg/jam)": [None], 
                    "Set Point Output Feeder Jotam S90 - Resin (kg/jam)": [None], 
                    "Aktual Output Feeder Jotam S90 - Resin (kg/jam)": [None], 
                    "Set Point Output Feeder Jotam S90 - Aditif (kg/jam)": [None], 
                    "Aktual Output Feeder Jotam S90 - Aditif (kg/jam)": [None], 
                    "Set Point Output Liquid Feeder (kg/jam)": [None], 
                    "Aktual Output Liquid Feeder (kg/jam)": [None], 
                    "Tekanan Liquid Feeder": [None], 
                    "RPM Main Feeder": [None], 
                    "Ampere Main Feeder": [None], 
                    "RPM Feeder Rework": [None], 
                    "RPM Side Feeder": [None] 
                    }
        df_data_page_2 = pd.DataFrame(nama_kolom_page_2)
        st.session_state.df_data_page_2 = df_data_page_2

        nama_kolom_page_3 = {
                    "Dokumentasi Panel Mesin Extruder":[None],
                    "Set Point Output Mesin": [None], 
                    "Aktual Output Mesin": [None], 
                    "Set Point Ampere & RPM Extruder": [None], 
                    "Aktual Ampere & RPM Extruder": [None], 
                    "SEI": [None], 
                    "Melt Temperature Extruder": [None], 
                    "Melt Pressure Extruder": [None], 
                    "Kondisi Valve Pendingin Barrel Zone 1": [None], 
                    "Set Point Temperature Zone 1": [None], 
                    "Aktual Temperature Zone 1": [None],
                    "Set Point Temperature Zone 2": [None], 
                    "Aktual Temperature Zone 2": [None],
                    "Set Point Temperature Zone 3": [None], 
                    "Aktual Temperature Zone 3": [None], 
                    "Set Point Temperature Zone 4": [None], 
                    "Aktual Temperature Zone 4": [None],
                    "Set Point Temperature Zone 5": [None], 
                    "Aktual Temperature Zone 5": [None],
                    "Set Point Temperature Zone 6": [None], 
                    "Aktual Temperature Zone 6": [None],
                    "Set Point Temperature Zone 7": [None], 
                    "Aktual Temperature Zone 7": [None],
                    "Set Point Temperature Zone 8": [None], 
                    "Aktual Temperature Zone 8": [None],
                    "Set Point Temperature Zone 9": [None], 
                    "Aktual Temperature Zone 9": [None],
                    "Set Point Temperature Zone 10": [None], 
                    "Aktual Temperature Zone 10": [None],
                    "Set Point Temperature Zone 11": [None], 
                    "Aktual Temperature Zone 11": [None],
                    "Set Point Temperature Zone 12": [None], 
                    "Aktual Temperature Zone 12": [None],
                    "Set Point Temperature 8.0": [None], 
                    "Aktual Temperature 8.0": [None], 
                    "Set Point Temperature Input Screen Changer": [None], 
                    "Aktual Temperature Input Screen Changer": [None], 
                    "Set Point Temperature TSW / Screen Changer 1": [None], 
                    "Aktual Temperature TSW / Screen Changer 1": [None], 
                    "Set Point Temperature Screen Changer 2": [None], 
                    "Aktual Temperature Screen Changer 2": [None], 
                    "Temperature Air Cooling Barrel Mesin (Soft Water)": [None],
                    "Temperature Air Cooling Gearbox (Cooling Water)": [None], 
                    "Tekanan Air Cooling Barrel Mesin": [None], 
                    "Temperature Oli Gearbox": [None] ,
                    "Vacuum Bar": [None],
                    "Tekanan Air Vacuum System":[None]
                    }
        df_data_page_3 = pd.DataFrame(nama_kolom_page_3)
        st.session_state.df_data_page_3 = df_data_page_3

        nama_kolom_page_4 = {
                    "Dokumentasi Panel UWP":[None],
                    "Set Point Temperature Adapter": [None], 
                    "Aktual Temperature Adapter": [None], 
                    "Set Point Temperature PoDV": [None], 
                    "Aktual Temperature PoDV": [None], 
                    "Set Point Temperature Die Plate": [None], 
                    "Aktual Temperature Die Plate": [None], 
                    "Set Point Temperature Water Tank": [None], 
                    "Aktual Temperature Water Tank": [None],
                    "Melt Pressure UWP": [None],
                    "Melt Temperature UWP": [None], 
                    "Ampere/Torsi Cutter": [None], 
                    "RPM Cutter": [None],
                    "Setting Maju Cutter": [None], 
                    "% Panjang Cutter": [None],
                    "Tekanan Air Proses UWP": [None], 
                    "Flow Air Proses UWP": [None], 
                    "Temperature In Air Proses": [None], 
                    "Temperature Out Air Proses": [None],
                    "Temperature In Air Cooling Tower": [None], 
                    "Temperature Out Air Cooling Tower": [None],
                    "Output Aktual FG": [None], 
                    "Jumlah Granule per Gram": [None],
                    "Perhitungan Jumlah Die Hole Terbuka": [None], 
                    }
        df_data_page_4 = pd.DataFrame(nama_kolom_page_4)
        st.session_state.df_data_page_4 = df_data_page_4
        


    st.markdown(f"<h3 style='text-align: left;'><br>HALAMAN 6/6 : QUANTITY REWORK</h3>", unsafe_allow_html=True)
    # st.markdown(f"<h3 style='text-align: center;'>EXTRUDER<br></h3>", unsafe_allow_html=True)
    # st.write(df_all_data)

    with st.form(key='form_page_5', clear_on_submit=False):

        tailing_rework = None
        gandeng_rework = None
        gramasi_rework = None
        homogen_rework = None
        phorous_rework = None
        tailing_rework = None
        disperse_rework = None

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK TAILING</h5>", unsafe_allow_html=True)
            tailing_rework = st.number_input("", key="tailing_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GANDENG/DEMPET</h5>", unsafe_allow_html=True)
            gandeng_rework = st.number_input("", key="gandeng_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HAZY</h5>", unsafe_allow_html=True)
            hazy_rework = st.number_input("", key="hazy_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK DISPERSE</h5>", unsafe_allow_html=True)
            disperse_rework = st.number_input("", key="disperse_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK GRAMASI</h5>", unsafe_allow_html=True)
            gramasi_rework = st.number_input("", key="gramasi_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK HOMOGEN</h5>", unsafe_allow_html=True)
            homogen_rework = st.number_input("", key="homogen_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK PHOROUS</h5>", unsafe_allow_html=True)
            phorous_rework = st.number_input("", key="phorous_rework", format="%d", step=1)

        with st.container(border=True):
            st.markdown(f"<h5 style='text-align: left;'>QUANTITY REWORK REKONDISI</h5>", unsafe_allow_html=True)
            rekondisi_rework = st.number_input("", key="rekondisi_rework", format="%d", step=1)

        can_submit = True

        if tailing_rework is None:
            can_submit = False
        
        if gandeng_rework is None:
            can_submit = False

        if hazy_rework is None:
            can_submit = False

        if disperse_rework is None:
            can_submit = False

        if gramasi_rework is None:
            can_submit = False

        if homogen_rework is None:
            can_submit = False

        if phorous_rework is None:
            can_submit = False

        if rekondisi_rework is None:
            can_submit = False

        with stylable_container(
            "dark blue",
            css_styles="""
            button {
                background-color: #283281 !important;
                color: white !important;
                border: none !important;
                transition: background-color 0.3s ease;
                margin-bottom: 20px !important;  /* Add space after button */
            }""",
        ):
            submit_button_5_1 = st.form_submit_button(label='Submit', width = "stretch")

        if submit_button_5_1:

            if can_submit == False:
                if tailing_rework is None:
                    st.toast('Isi bagian "Quantity Rework Tailing"!', icon="⚠️")
                
                if gandeng_rework is None:
                    st.toast('Isi bagian "Quantity Rework Gandeng/Dempet"!', icon="⚠️")
        
                if hazy_rework is None:
                    st.toast('Isi bagian "Quantity Rework Hazy"!', icon="⚠️")
        
                if disperse_rework is None:
                    st.toast('Isi bagian "Quantity Rework Disperse"!', icon="⚠️")
        
                if gramasi_rework is None:
                    st.toast('Isi bagian "Quantity Rework Gramasi"!', icon="⚠️")
        
                if homogen_rework is None:
                    st.toast('Isi bagian "Quantity Rework Homogen"!', icon="⚠️")
        
                if phorous_rework is None:
                    st.toast('Isi bagian "Quantity Rework Phorous"!', icon="⚠️")
        
                if rekondisi_rework is None:
                    st.toast('Isi bagian "Quantity Rework Rekondisi"!', icon="⚠️")
                    
                st.error(f"Lengkapi seluruh kolom sebelum menekan tombol Submit!")
                
            else:
                nama_kolom_page_5 = {
                    "Quantity Rework Tailing": [], 
                    "Quantity Rework Gandeng/Dempet": [], 
                    "Quantity Rework Hazy": [], 
                    "Quantity Rework Disperse": [], 
                    "Quantity Rework Gramasi": [], 
                    "Quantity Rework Homogen": [], 
                    "Quantity Rework Phorous": [], 
                    "Quantity Rework Rekondisi": [],  
                    }
                df_data_page_5 = pd.DataFrame(nama_kolom_page_5)

                new_row_page_5 = pd.DataFrame({
                    "Quantity Rework Tailing": [tailing_rework], 
                    "Quantity Rework Gandeng/Dempet": [gandeng_rework], 
                    "Quantity Rework Hazy": [hazy_rework], 
                    "Quantity Rework Disperse": [disperse_rework], 
                    "Quantity Rework Gramasi": [gramasi_rework], 
                    "Quantity Rework Homogen": [homogen_rework], 
                    "Quantity Rework Phorous": [phorous_rework], 
                    "Quantity Rework Rekondisi": [rekondisi_rework] 
                })
                df_data_page_5 = pd.concat([df_data_page_5, new_row_page_5]).reset_index(drop=True)
                st.success(f'Cek apakah data berikut sudah benar? Apabila sudah maka tekan tombol "Next Page"')
                st.write(df_data_page_5.dropna(axis=1, inplace=False))
                st.session_state.df_data_page_5 = df_data_page_5
    

    with st.container(horizontal=True):
        back_button_5 = st.button("◀️ Kembali", width="stretch")
        submit_button_2_5 = st.button(type="primary", label='Next Page ➔', width="stretch")
        
                
    if submit_button_2_5:
        if "df_data_page_5" not in st.session_state:
            # st.error(f'Lengkapi seluruh kolom dan tekan tombol "Submit" sebelum menekan tombol "Next Page"!')
            st.toast(f'Tekan tombol "Submit" sebelum menekan tombol "Next Page"!', icon="❌")
            # time.sleep(2)
        else:
            st.session_state.page = 6
            st.session_state.scroll_to_top = True
            st.rerun()
            

        

    @st.dialog("Apakah Anda yakin akan kembali ke halaman sebelumnya?")
    def backpage_5():
        with st.container(horizontal=True):
            button_no_5 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_5 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_5:
                if 'df_data_page_5' in st.session_state:
                    del st.session_state['df_data_page_5']
                if df_data_page_1["Kondisi Mesin"][0] == 'Running':
                    del st.session_state['df_data_page_4']
                    st.session_state.page = 4 
                else:
                    del st.session_state['df_data_page_1']
                    st.session_state.page = 1
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_5:
                st.rerun()
                
    if back_button_5:
        backpage_5()
        
        

    back_button_5_to_1 = st.button("⏪ Kembali ke Halaman 1")

    @st.dialog("Apakah Anda yakin akan kembali ke halaman awal?")
    def backpage_5_to_1():
        with st.container(horizontal=True):
            button_no_5_to_1 = st.button(label='Tidak', width="stretch", type="secondary")
            button_yes_5_to_1 = st.button(label='Ya', width="stretch", type="primary")

            if button_yes_5_to_1:
                if 'df_data_page_6' in st.session_state:
                    del st.session_state['df_data_page_6']
                if df_data_page_1["Kondisi Mesin"][0] == 'Running':
                    del st.session_state['df_data_page_5']
                    del st.session_state['df_data_page_4']
                    del st.session_state['df_data_page_3']
                    del st.session_state['df_data_page_2']
                    del st.session_state['df_data_page_1_5']
                    del st.session_state['df_data_page_1']
                else :
                    del st.session_state['df_data_page_1']
                st.session_state.page = 1
                st.session_state.scroll_to_top = True
                st.rerun()

            if button_no_5_to_1:
                st.rerun()
                
    if back_button_5_to_1:
        backpage_5_to_1()
    
        
        

#Halaman 6
if st.session_state["page"] == 6:
    if st.session_state.get("scroll_to_top", False):
        scroll_to_top()
        st.session_state.scroll_to_top = False
     
    
    df_data_page_1 = st.session_state.df_data_page_1
    df_data_page_2 = st.session_state.df_data_page_2
    df_data_page_3 = st.session_state.df_data_page_3
    df_data_page_4 = st.session_state.df_data_page_4
    df_data_page_5 = st.session_state.df_data_page_5
    submit_time_now = datetime.now()
    submit_time = pd.DataFrame({
                    "Submit Time": [submit_time_now]
                })

    all_df_new_row = pd.concat([df_data_page_1, df_data_page_2, df_data_page_3, df_data_page_4, df_data_page_5, submit_time], axis=1)

    new_df = save_data(all_df_new_row)

    

    st.markdown(
        """
        <h2 style='text-align: center; color: green;'>
            ✅ Terima Kasih!
        </h2>
        <h4 style='text-align: center;'>
            Terima kasih telah mengisi <b>e-Monitoring Produksi</b>.
        </h4>
        <p style='text-align: center;'>
            Data yang Anda masukkan sudah tersimpan dengan baik.
        </p>
        """,
        unsafe_allow_html=True
    )
