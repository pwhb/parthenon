function lowercase(s) {
    return s.toLowerCase();
}

const params = process.argv.slice(2);
async function main() {
    console.log("\n\n\n");
    const input = params[0]
    console.log(lowercase(input));
    
    console.log("\n\n\n");
}

main().catch(console.error).finally(() => process.exit(0));