import axios from "axios";
import React, {useState} from "react";
import { toast } from "react-toastify";
import { json, useNavigate,Link } from "react-router-dom";

const Login= () =>{
    const navigate=useNavigate()
    const [logindata, setLogindata]=useState({
        email:'',
        password:''
    })
    const [error,setError] =useState("")
    const [isLoding,setIsLoading]=useState(false)
    const handleOnChange=(e)=>{
        setLogindata({...logindata,[e.target.name]:e.target.value})
    }
    const handleSubmit =async (e)=>{
        e.preventDefault()
        const {email,password}=logindata
        if (!email || !password){
            setError('email and password are required')
        }else{
            setIsLoading(true)
            console.log(logindata)
            const res =await axios.post("http://localhost:8000/api/v1/auth/login/",logindata)
            const response=res.data
            setIsLoading(false)
            const user={
                "email":response.email,
                "names":response.full_name
            }
            if (res.status ===200){
                localStorage.setItem("user",JSON.stringify(user))
                localStorage.setItem("access",JSON.stringify(response.access_token))
                localStorage.setItem("refresh",JSON.stringify(response.refresh_token))
                navigate("/dashboard")
                toast.success('login successfull')
            }
        }
    }
    return (
            <div>
            <div className="form-container">
                <div style={{width:"100%"}} className="wrapper">
                    <h2>Login</h2>
                    <form onSubmit={handleSubmit}>
                        {isLoding && (
                            <p>Loading ....</p>
                        )}
                        <div className="form-group">
                            <label htmlFor="">Email Address: </label>
                            <input type='text' className="email-form" name="email" 
                            value={logindata.email} 
                            onChange={handleOnChange}/>
                        </div>
                        <div className="form-group">
                            <label htmlFor="">Password: </label>
                            <input type='password' className="email-form" name="password" 
                            value={logindata.password} 
                            onChange={handleOnChange}/>
                        </div>
                        
                        <input type="submit" value="Login" className="submitButton"/>
                        <p className="pass-link"><Link to={'/forget_password'}>ForgetPassword</Link></p>
                    </form>
                    
                </div>
            </div>
        </div>
    )
}
export default Login