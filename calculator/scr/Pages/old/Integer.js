import React, {Component} from 'react'
import Calculate from '../../Calculate'
import styles from './Calculate.module.css'
import logo from './foto.jpg'
export default class Integer extends Component {
    constructor(){
        super()
        this.state={
            out: '0'
        }
    }
    tapeNumber(value){
        let currentValue=value
        let output=this.refoutput.current
        this.setState({
            out:currentValue
        })

        if (output.value === '0') {output.value=''}
        output.value += currentValue
    }

    tapeOperation(value){
        let output=this.refoutput.current

        if (value ==='CE'){
            if (output.value.length===1){output.value ='0'} else {
                output.value= output.value.substring(0,output.value.length-1)
            }
             
        }

        else if (value === 'AC') {output.value = '0'}
       
        else if (value === '=') {
            try {output.value=eval(output.value)}
            catch {
                output.value = 'Недопустимое значение'
                
            }
        }
    }    
    
    render() {
        
        return (
            <div >
            <div className={styles.imageBox}>
                <img src={logo} alt="Image1"style={{position: "absolute",height: "400px",width: "100%",top: "20%"}}/>
            </div>
            
            <h1 style={{position: "absolute",top: "10%",left: "41%",fontSize: 45}}>Mode: Integer</h1>

            <div className={styles.container2}> 
                 <div>
                      
                      <input  ref={this.refoutput} type="text" defaultValue={this.state.out} 
                      style={{position: "absolute",top: "14%",left: "14%", width: "550px",border: "5px"}} />
                 </div>

                 
            </div>
            <div className={styles.container}>
               
                
                <div className="buttons">
                    {Calculate.buttons.map((item)=> {
                        return <button 
                        onClick={()=>{this.tapeNumber(item.val)}}
                        >{item.val}
                        </button>})
                    }

                    {Calculate.operations.map((item)=> {
                        return <button 
                        onClick={()=>{this.tapeOperation(item.val)}}
                        >{item.val}
                        </button>})
                    }
                </div>
            </div>
            </div>
        )
    }
}
