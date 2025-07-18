import React, {useState} from "react";
import { useNavigate, useParams } from "react-router-dom";
import axiosInstance from "../utils/axiosinstance";
import { toast } from "react-toastify";

const RestPassword = () =>{
    const navigate=useNavigate()
    const {uid, token}=useParams()
    const [newpasswords,setNewPasswords]=useState({
        password:'',
        confirm_password:''
    })
    const handleChange=(e)=>{
        setNewPasswords({...newpasswords,[e.target.name]:e.target.value})
    }
    const data={
        'password':newpasswords.password,
        'confirm_password':newpasswords.confirm_password,
        'uidb64':uid,
        'token':token
    }
    const handleSubmit= async (e)=>{
        e.preventDefault()
        // make api call
        const response = axiosInstance.patch('/auth/set-new-password',data)
        const result = response.data
        if (result.status === 200){
            navigate('/login')
            toast.success(result.message)
        }
        console.log(response)
    }
    return (
        <div>
            <div className='form-container'>
                <div className="wrapper" style={{width:"100%"}}>
                    <h2>Enter your new password</h2>
                    <form action="" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="">New Password:</label>
                            <input type="text" className="email-form" name="password" 
                            value={newpasswords.password} onChange={handleChange} />    
                        </div>
                        <div>
                            <label htmlFor="">Confirm Password</label>
                            <input type="text" className="email-form" name="confirm_password" 
                            value={newpasswords.confirm_password} 
                            onChange={handleChange} />
                        </div>
                        <button type="submit" className="vbtn">Submit</button>
                    </form>
                </div>
            </div>    
        </div>
    )
}

export default RestPassword