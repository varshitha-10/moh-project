// MongoDB sample collections and seed data
const { MongoClient } = require('mongodb');
const uri = 'mongodb://user:password@mongo:27017';
const client = new MongoClient(uri);

async function seed() {
  try {
    await client.connect();
    const db = client.db('testdb');
    // user_profiles
    await db.collection('user_profiles').insertMany(Array.from({length:20}, (_,i)=>({user_id:i+1,name:`User${i+1}`,email:`user${i+1}@example.com`})));
    // product_catalogs
    await db.collection('product_catalogs').insertMany(Array.from({length:20}, (_,i)=>({product_id:i+1,name:`Product${i+1}`,price:Math.round(Math.random()*1000)/10})));
    // activity_logs
    await db.collection('activity_logs').insertMany(Array.from({length:20}, (_,i)=>({log_id:i+1,action:`Action${i+1}`,timestamp:new Date()})));
    // recommendations
    await db.collection('recommendations').insertMany(Array.from({length:20}, (_,i)=>({rec_id:i+1,user_id:(i%20)+1,product_id:(i%20)+1})));
    console.log('MongoDB seed complete');
  } finally {
    await client.close();
  }
}
seed();
