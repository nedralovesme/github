export function readUser(){
    console.log("reading a user");
    return {
        type:"READ_USER",
        payload:{name:"Bob",age:68},
    }
}
