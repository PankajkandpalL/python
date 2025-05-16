import React, { useState } from 'react';
import { Modal, View, Text, TouchableOpacity, StyleSheet, Pressable } from 'react-native';

const PaymentModal = ({ visible, onClose, onPay }) => {
  const [walletOption, setWalletOption] = useState('PL Wallet');
  const [gatewayOption, setGatewayOption] = useState('Plur');

  return (
    <Modal
      visible={visible}
      animationType="slide"
      transparent
      onRequestClose={onClose}
    >
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.title}>Choose Payment Mode</Text>
          <View style={styles.divider} />

          <Text style={styles.section}>Wallet</Text>
          <View style={styles.optionBox}>
            {['PL Wallet', 'PL Currency'].map((option, idx) => (
              <React.Fragment key={option}>
                <TouchableOpacity
                  style={styles.optionRow}
                  onPress={() => setWalletOption(option)}
                >
                  <View style={[styles.colorBox, {
                    backgroundColor: option === 'PL Wallet' ? 'green' : 'orange'
                  }]} />
                  <Text style={styles.optionText}>{option}</Text>
                  <Text style={styles.credit}>₹100.00</Text>
                  <View style={styles.radioCircle}>
                    {walletOption === option && <View style={styles.selectedRb} />}
                  </View>
                </TouchableOpacity>
                {idx < 1 && <View style={styles.innerDivider} />}
              </React.Fragment>
            ))}
          </View>

          <Text style={styles.section}>Payment gateway</Text>
          <View style={styles.optionBox}>
            {['Plur', 'Pay U'].map((option, idx) => (
              <React.Fragment key={option}>
                <TouchableOpacity
                  style={styles.optionRow}
                  onPress={() => setGatewayOption(option)}
                >
                  <Text style={[styles.optionText, { marginLeft: 5 }]}>{option}</Text>
                  <View style={styles.radioCircle}>
                    {gatewayOption === option && <View style={styles.selectedRb} />}
                  </View>
                </TouchableOpacity>
                {idx < 1 && <View style={styles.innerDivider} />}
              </React.Fragment>
            ))}
          </View>

          <Pressable style={styles.payButton} onPress={onPay}>
            <Text style={styles.payText}>Pay</Text>
          </Pressable>
        </View>
      </View>
    </Modal>
  );
};

export default PaymentModal;

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.4)',
    justifyContent: 'flex-end',
  },
  modal: {
    backgroundColor: 'white',
    padding: 20,
    borderTopRightRadius: 15,
    borderTopLeftRadius: 15,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    marginBottom: 10,
  },
  divider: {
    height: 1,
    backgroundColor: '#ccc',
    marginBottom: 15,
  },
  section: {
    fontSize: 14,
    fontWeight: '500',
    marginTop: 10,
    marginBottom: 8,
  },
  optionBox: {
    backgroundColor: '#F5F5F5',
    borderRadius: 8,
    paddingVertical: 5,
    marginBottom: 20,
  },
  optionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingVertical: 12,
  },
  innerDivider: {
    height: 1,
    backgroundColor: '#DDD',
    marginHorizontal: 10,
  },
  colorBox: {
    width: 12,
    height: 12,
    borderRadius: 2,
    marginRight: 10,
  },
  optionText: {
    flex: 1,
    fontSize: 16,
  },
  credit: {
    fontSize: 14,
    color: 'gray',
    marginRight: 10,
  },
  radioCircle: {
    height: 20,
    width: 20,
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: '#000',
    alignItems: 'center',
    justifyContent: 'center',
  },
  selectedRb: {
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: '#000',
  },
  payButton: {
    marginTop: 10,
    backgroundColor: '#000',
    paddingVertical: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  payText: {
    color: 'white',
    fontSize: 16,
    fontWeight: '600',
  },
});
