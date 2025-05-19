import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  FlatList,
  TextInput,
} from 'react-native';

const WalletScreen = () => {
  const [wallets, setWallets] = useState([
    { id: '1', name: 'PL Wallet', balance: 1000 },
    { id: '2', name: 'PL Currency', balance: 1000 },
  ]);

  const [selectedWalletId, setSelectedWalletId] = useState(null);
  const [enteredAmount, setEnteredAmount] = useState('');

  const addAmount = (walletId) => {
    const amount = parseFloat(enteredAmount);
    if (isNaN(amount) || amount <= 0) return;

    setWallets((prevWallets) =>
      prevWallets.map((wallet) =>
        wallet.id === walletId
          ? { ...wallet, balance: wallet.balance + amount }
          : wallet
      )
    );
    setEnteredAmount('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Wallets & payments</Text>

      <FlatList
        data={wallets}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => {
          const isSelected = item.id === selectedWalletId;
          return (
            <TouchableOpacity
              style={styles.walletBox}
              onPress={() => setSelectedWalletId(item.id)}
              activeOpacity={0.8}
            >
              <Text style={styles.walletName}>{item.name}</Text>
              <Text style={styles.walletBalance}>₹{item.balance.toFixed(2)}</Text>

              {isSelected && (
                <View style={styles.addMoneyBox}>
                  <TextInput
                    placeholder="Enter amount"
                    value={enteredAmount}
                    onChangeText={setEnteredAmount}
                    keyboardType="numeric"
                    style={styles.input}
                  />
                  <TouchableOpacity
                    style={styles.addMoneyButton}
                    onPress={() => addAmount(item.id)}
                  >
                    <Text style={styles.addMoneyText}>Add Money</Text>
                  </TouchableOpacity>
                </View>
              )}
            </TouchableOpacity>
          );
        }}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#fff', flex: 1 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  walletBox: {
    backgroundColor: '#fff',
    borderColor: '#ccc',
    borderWidth: 1,
    padding: 16,
    borderRadius: 10,
    marginBottom: 15,
  },
  walletName: { fontSize: 16, fontWeight: '600' },
  walletBalance: { fontSize: 16, marginTop: 4 },
  addMoneyBox: { marginTop: 15 },
  input: {
    borderColor: '#ccc',
    borderWidth: 1,
    borderRadius: 8,
    padding: 10,
    fontSize: 16,
    marginBottom: 10,
  },
  addMoneyButton: {
    backgroundColor: '#004d40',
    padding: 12,
    borderRadius: 8,
    alignItems: 'center',
  },
  addMoneyText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '500',
  },
});

export default WalletScreen;