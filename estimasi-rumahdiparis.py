import pickle
import streamlit as st

model = pickle.load(open('estimasi_rumahdiparis.sav','rb'))

st.title('Estimasi Harga Rumah di Paris')

squareMeters = st.number_input('Input Luas Lahan')
numberOfRooms = st.number_input('Input Nomor Ruangan')
floors = st.number_input('Input Lantai')
numPrevOwners = st.number_input('Input Jumlah Pemilik yang pernah beli rumah ini')
basement = st.number_input('Input basement')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[squareMeters, numberOfRooms, floors, numPrevOwners, basement]]
    )
    st.write ('Estimasi harga rumah dalam Dollar : ', predict)
    st.write ('Estimasi harga rumah dalam IDR (Juta) :', predict*15000)