const list = ["hannibal", "twin peaks", "westworld", "neon genesis evangelion", "bojack horseman", "futurama", "dark", "la casa de papel", "mr robot", "daredevil ", "the twilight zone", "black mirror", "attack on titans", "jojo's bizarre adventure", "death note", "breaking bad", "doctor who", "strangers from hell", "welcome to nhk", "squid game"
]

const random = list.sort(() => 0.5 - Math.random())

console.log(random)