import React, { useEffect,useRef,useState } from 'react';
import { Link } from 'react-router-dom';
import { PieChart, Pie, Cell ,Sector} from 'recharts';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { gsap } from 'gsap/all';
import axios from "axios";

export default function Dashboard() {
const [aws_ec2_info, setaws_ec2_info] = useState({});
const [azure_info, setazure_info] = useState({});
const [awsgraph2, setawsgraph2] = useState({});
const [azuregraph2, setazuregraph2] = useState({});
const [awsgraph3, setawsgraph3] = useState({});
const [azuregraph3, setazuregraph3] = useState({});
const [awsgraph4, setawsgraph4] = useState({});
const [azuregraph4, setazuregraph4] = useState({});
const [awsgraph5, setawsgraph5] = useState({});
const [azuregraph5, setazuregraph5] = useState({});

  useEffect(() => {
      var tl=gsap.timeline();
      tl.to('.intro', { opacity: 0, duration: 1, delay:0.5 },);
      tl.to('.intro', { visibility:"hidden" });
      tl.to('.intro2', { opacity: 1, duration: 1, delay:0.5 });
      tl.to('.intro2', { opacity: 0, duration: 1, delay:0.5 });
      tl.to('.intro2', { visibility:"hidden" });
      tl.from('.centerlayer', { opacity: 0, duration: 3,y: -100 },"start");
tl.from('.leftlayer', { opacity: 0, duration: 3, x: -100 },"start");
tl.from('.rtcontainer', { opacity: 0, duration: 3, x: 100 },"start");
tl.from('.bcontainer', { opacity: 0, duration: 3, y: 100 },"start");
      if(!holder){
          if(!loader){
                gsap.set(".lineseg", { width: 0 });
      gsap.to(".lineseg", {
                    duration: 1.75,
                    width: '100%',
                    stagger: 0.095,
                })
          }
      }
  }, []);

  const [instance_memory, setinstance_memory] = useState('0.5');
    const [vcpus, setvcpus] = useState('1');
    const [avgcpu_usage, setavgcpu_usage] = useState('0');
    const [vmmemorybucket, setvmmemorybucket] = useState('0');
    const [vmcreated, setvmcreated] = useState('0');
    const [vmdeleted, setvmdeleted] = useState('0');
    const [vmcorecountbucket, setvmcorecountbucket] = useState('0');
    const [bucket, setbucket] = useState("low");
    const [prediction, setPrediction] = useState(null);
    const [prediction2, setPrediction2] = useState(null);
    const [prediction3, setPrediction3] = useState(null);
    const [prediction4, setPrediction4] = useState(null);
    const [prediction5, setPrediction5] = useState(null);
    const [azure1, setazure1] = useState(null);
    const [azure2, setazure2] = useState(null);
    const [azure3, setazure3] = useState(null);
    const [azure4, setazure4] = useState(null);
    const [azure5, setazure5] = useState(null);
    const [aws1, setaws1] = useState(null);
    const [aws2, setaws2] = useState(null);
    const [aws3, setaws3] = useState(null);
    const [aws4, setaws4] = useState(null);
    const [aws5, setaws5] = useState(null);
    const [title1, settitle1] = useState(null);
    const [title2, settitle2] = useState(null);
    const [title3, settitle3] = useState(null);
    const [title4, settitle4] = useState(null);
    const [title5, settitle5] = useState(null);
    const [autoscale, setautoscale] = useState(null);
    const [loader, setloader] = useState(false);
    const [holder, setholder] = useState(true);

    const options = [
        '0.5', '1.0', '0.75', '2.0', '4.0', '1.75', '8.0', '3.5', '16.0', '7.0', '14.0', '32.0', '28.0', '84.0',
        '64.0', '55.0', '48.0', '56.0', '128.0', '80.0', '110.0', '160.0', '252.0', '112.0', '219.0', '240.0', '220.0',
        '208.0', '96.0', '192.0', '256.0', '140.0', '504.0', '224.0', '384.0', '144.0', '480.0', '438.0', '352.0', '440.0',
        '756.0', '456.0', '448.0', '512.0', '432.0', '1008.0', '880.0', '288.0', '672.0', '875.0', '974.0', '640.0',
        '1024.0', '768.0', '1750.0', '656.0', '1300.0', '1792.0', '1946.0', '2048.0', '3800.0', '2794.0', '2850.0',
        '3892.0', '900.0', '4096.0', '1923.0', '5700.0', '7600.0', '11400.0', '176.0', '6144.0', '3072.0', '1536.0',
        '8192.0', '12000.0', '12288.0', '3840.0', '18432.0', '9216.0', '5760.0', '4608.0', '24576.0', '7680.0', '3.75',
        '5.25', '15.25', '6.0', '7.5', '10.5', '30.5', '12.0', '15.0', '21.0', '61.0', '24.0', '30.0', '122.0', '42.0',
        '72.0', '60.0', '244.0', '488.0', '976.0', '1952.0', '732.0', '3904.0', '1152.0', '0.613', '1.7', '17.1', '34.2',
        '68.4', '117.0', '60.5'
    ];
    const options2 = ['1', '2', '4', '8', '6', '16', '12', '20', '32', '18', '48', '10', '64', '24', '60', '72', '44', '36', '96', '120', '80', '40', '176', '104', '112', '128', '192', '208', '416', '224', '384', '448', '576', '672', '896'];


const handleInputChange = (e) => {
        const value = e.target.value.trim();
        const inputName = e.target.name;

        switch (inputName) {
            case 'instance_memory':
                setinstance_memory(value);
                break;
            case 'vcpus':
                setvcpus(value);
                break;
            case 'avgcpu_usage':
                setavgcpu_usage(value);
                break;
            case 'vmmemorybucket':
                setvmmemorybucket(value);
                break;
            case 'vmdeleted':
                setvmdeleted(value);
                break;
            case 'vmcreated':
                setvmcreated(value);
                break;
            case 'vmcorecountbucket':
                setvmcorecountbucket(value);
                break;
            case 'bucket':
                setbucket(value);
                break;
            default:
                break;
        }
    };

const handleSubmit = async (event) => {
    event.preventDefault();
    try {
        setloader(true);
        setholder(false);

        const response = await
            // axios.post('http://localhost:8000/MainApp/sample/',
                await axios.post('http://43.204.220.52/MainApp/sample/',
                {
            instance_memory: instance_memory,
            vcpus: vcpus,
            avgcpu_usage: avgcpu_usage,
            vmmemorybucket: vmmemorybucket,
            bucket: bucket,
            vmcreated: vmcreated,
            vmdeleted: vmdeleted,
            vmcorecountbucket: vmcorecountbucket
        });

        if (response && response.data) {
            setPrediction(response.data.prediction);
            setautoscale(response.data.autoscale);
            setazure_info(response.data.azure_info);
            setaws_ec2_info(response.data.aws_ec2_info);
            setPrediction2(response.data.prediction2);
            setPrediction3(response.data.prediction3);
            setPrediction4(response.data.prediction4);
            setPrediction5(response.data.prediction5);
            setazuregraph2(response.data.azuregraph2);
            setawsgraph2(response.data.awsgraph2);
            setazuregraph3(response.data.azuregraph3);
            setawsgraph3(response.data.awsgraph3);
            setazuregraph4(response.data.azuregraph4);
            setawsgraph4(response.data.awsgraph4);
            setazuregraph5(response.data.azuregraph5);
            setawsgraph5(response.data.awsgraph5);
        } else {
            console.error('Response data is undefined or null');
        }

        setloader(false);
        if (response.data.azure_info && response.data.azure_info.Microsoft_Azure && response.data.azure_info.Microsoft_Azure.On_Demand) {
                setazure1(parseFloat(response.data.azure_info.Microsoft_Azure.On_Demand));
                settitle1(azure_info.Microsoft_Azure.Instance_Memory+"+"+azure_info.Microsoft_Azure.vCPUs);
            }
            if (response.data.aws_ec2_info && response.data.aws_ec2_info.Amazon_EC2 && response.data.aws_ec2_info.Amazon_EC2.On_Demand) {
                setaws1(parseFloat(response.data.aws_ec2_info.Amazon_EC2.On_Demand));
            }
            if (response.data.azuregraph2 && response.data.azuregraph2.Microsoft_Azure && response.data.azuregraph2.Microsoft_Azure.On_Demand) {
                setazure2(parseFloat(response.data.azuregraph2.Microsoft_Azure.On_Demand));
                settitle2(azuregraph2.Microsoft_Azure.Instance_Memory+"+"+azuregraph2.Microsoft_Azure.vCPUs);
            }
            if (response.data.awsgraph2 && response.data.awsgraph2.Amazon_EC2 && response.data.awsgraph2.Amazon_EC2.On_Demand) {
                setaws2(parseFloat(response.data.awsgraph2.Amazon_EC2.On_Demand));
            }
            if (response.data.azuregraph3 && response.data.azuregraph3.Microsoft_Azure && response.data.azuregraph3.Microsoft_Azure.On_Demand) {
                setazure3(parseFloat(response.data.azuregraph3.Microsoft_Azure.On_Demand));
                settitle3(azuregraph3.Microsoft_Azure.Instance_Memory+"+"+azuregraph3.Microsoft_Azure.vCPUs);
            }
            if (response.data.awsgraph3 && response.data.awsgraph3.Amazon_EC2 && response.data.awsgraph3.Amazon_EC2.On_Demand) {
                setaws3(parseFloat(response.data.awsgraph3.Amazon_EC2.On_Demand));
            }
            if (response.data.azuregraph4 && response.data.azuregraph4.Microsoft_Azure && response.data.azuregraph4.Microsoft_Azure.On_Demand) {
                setazure4(parseFloat(response.data.azuregraph4.Microsoft_Azure.On_Demand));
                settitle4(azuregraph4.Microsoft_Azure.Instance_Memory+"+"+azuregraph4.Microsoft_Azure.vCPUs);
            }
            if (response.data.awsgraph4 && response.data.awsgraph4.Amazon_EC2 && response.data.awsgraph4.Amazon_EC2.On_Demand) {
                setaws4(parseFloat(response.data.awsgraph4.Amazon_EC2.On_Demand));
            }
            if (response.data.azuregraph5 && response.data.azuregraph5.Microsoft_Azure && response.data.azuregraph5.Microsoft_Azure.On_Demand) {
                setazure5(parseFloat(response.data.azuregraph5.Microsoft_Azure.On_Demand));
                settitle5(azuregraph5.Microsoft_Azure.Instance_Memory+"+"+azuregraph5.Microsoft_Azure.vCPUs);
            }
            if (response.data.awsgraph5 && response.data.awsgraph5.Amazon_EC2 && response.data.awsgraph5.Amazon_EC2.On_Demand) {
                setaws5(parseFloat(response.data.awsgraph5.Amazon_EC2.On_Demand));
            }
    } catch (error) {
        console.error('Error:', error);
    }
};


const data = [
  {
    name: '0',
    Microsoft_Azure_Cost: 0,
    Predicted_Cost: 0,
    Amazon_EC2: 0,
    amt: 0,
  },
  {
    name: title1 ? title1 : null,
    Microsoft_Azure_Cost: azure1 ? parseFloat((azure1 * 720).toFixed(2)) : 0,
    Predicted_Cost: prediction ? parseFloat((prediction * 720).toFixed(2)) : 0,
    Amazon_EC2: aws1 ? parseFloat((aws1 * 720).toFixed(2)) : 0,
    amt: 100,
  },
    {
      name: title2 ? title2 : null,
      Microsoft_Azure_Cost: azure2 ? parseFloat((azure2 * 720).toFixed(2)) : 0,
      Predicted_Cost: prediction2 ? parseFloat((prediction2 * 720).toFixed(2)) : 0,
      Amazon_EC2: aws2 ? parseFloat((aws2 * 720).toFixed(2)) : 0,
      amt: 200,
    },
    {
      name: title3 ? title3 : null,
      Microsoft_Azure_Cost: azure3 ? parseFloat((azure3 * 720).toFixed(2)) : 0,
      Predicted_Cost: prediction3 ? parseFloat((prediction3 * 720).toFixed(2)) : 0,
      Amazon_EC2: aws3 ? parseFloat((aws3 * 720).toFixed(2)) : 0,
      amt: 300,
    },
    {
      name: title4 ? title4 : null,
      Microsoft_Azure_Cost: azure4 ? parseFloat((azure4 * 720).toFixed(2)) : 0,
      Predicted_Cost: prediction4 ? parseFloat((prediction4 * 720).toFixed(2)) : 0,
      Amazon_EC2: aws4 ? parseFloat((aws4 * 720).toFixed(2)) : 0,
      amt: 400,
    },
    {
      name: title5 ? title5 : null,
      Microsoft_Azure_Cost: azure5 ? parseFloat((azure5 * 720).toFixed(2)) : 0,
      Predicted_Cost: prediction5 ? parseFloat((prediction5 * 720).toFixed(2)) : 0,
      Amazon_EC2: aws5 ? parseFloat((aws5 * 720).toFixed(2)) : 0,
      amt: 500,
    },
  ];

    const style = {
        background: 'linear-gradient(90deg,#808080,#808080,#808080, #fcfffd, #808080,#808080,#808080,#fcfffd, #808080,#808080,#808080,#fcfffd,#808080,#808080,#808080)',
        backgroundSize: '400%',
        WebkitTextFillColor: 'transparent',
        WebkitBackgroundClip: 'text',
        animation: 'animate 50s linear infinite'
    };
    return (
        <div className="w-full h-screen overflow-hidden flex items-center justify-center">
            <div className="intro w-full h-full flex items-center justify-center absolute">
                <h1 className="font-['PP', 'Helvetica', 'Arial', 'sans-serif'] text-[100px]">NOVA PRESENTS</h1>
            </div>
            <div className="intro2 w-full h-full flex items-center justify-center absolute opacity-0">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-28 h-28 mr-4">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15a4.5 4.5 0 0 0 4.5 4.5H18a3.75 3.75 0 0 0 1.332-7.257 3 3 0 0 0-3.758-3.848 5.25 5.25 0 0 0-10.233 2.33A4.502 4.502 0 0 0 2.25 15Z" />
</svg>
                <h1 className="font-['PP', 'Helvetica', 'Arial', 'sans-serif'] text-[100px]">
                    Zenith
                </h1>
            </div>
            <div className="h-full w-full px-4 py-4">
                <div className="grid gap-4 grid-cols-3 w-full h-full rounded-3xl px-4 py-4">
                    <div className="leftlayer col-span-1 grid grid-rows-7 bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl">
                        <div className="row-span-1 w-full h-full rounded-3xl flex items-center justify-center">
                            <h className="text-2xl tracking-widest font-normal bg-black text-white px-4 rounded-xl h-8" style={style}>Total Cost of Ownership</h>
                            <style>
                            {`
          @keyframes animate {
            0% {
              background-position: 400%;
            }
            100% {
              background-position: 0%;
            }
          }
        `}
                        </style>
                        </div>
                        <div className="row-span-6 w-full h-full rounded-3xl">
                            <form className="grid grid-rows-6 w-full h-full rounded-b-3xl" onSubmit={handleSubmit}>
                                <div className="grid grid-cols-2 w-full h-full row-span-5">
                                    <div className="grid grid-rows-4 w-full h-full">
                                        <div className="w-full h-full items-center justify-center grid grid-rows-3">
                                            <div className="w-full h-full flex justify-center items-center">
                                                Instance Memory
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                                <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="instance_memory"
                                                id="Type"
                                                value={instance_memory} onChange={handleInputChange}
                                            >
                                                {options.map((option, index) => (
                                                    <option key={index} value={option}>{option} GiB</option>
                                                ))}
                                            </select>
                                            </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                vCPUs
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                                <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="vcpus"
                                                id="Type"
                                                value={vcpus} onChange={handleInputChange}
                                            >
                                                {options2.map((options2, index) => (
                                                    <option key={index} value={options2}>{options2} vCPUs</option>
                                                ))}
                                            </select>
                                            </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                Average CPU Usage
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="avgcpu_usage"
                                                id="Type"
                                                type="text"
                                                value={avgcpu_usage}
                                                onChange={handleInputChange}
                                                placeholder="Average CPU Usage"
                                            />
                                        </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                VM Created
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="vmcreated"
                                                id="Type"
                                                type="text"
                                                value={vmcreated}
                                                onChange={handleInputChange}
                                                placeholder="VM Created"
                                            />
                                        </div>
                                        </div>
                                    </div>
                                    <div className="grid grid-rows-4 w-full h-full">
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                VM Memory Bucket
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">

                                        <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="vmmemorybucket"
                                                id="Type"
                                                type="text"
                                                value={vmmemorybucket}
                                                onChange={handleInputChange}
                                                placeholder="VM Memory Bucket"
                                            />
                                        </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                Budget
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                            <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="bucket"
                                                id="Type"
                                                value={bucket}
                                                onChange={handleInputChange}
                                            >
                                                <option value="low">Low Budget</option>
                                                <option value="medium">Medium Budget</option>
                                                <option value="high">High Budget</option>
                                                <option value="very high">Very High Budget</option>
                                            </select>
                                        </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                Bucket Count
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="vmcorecountbucket"
                                                id="Type"
                                                type="text"
                                                value={vmcorecountbucket}
                                                onChange={handleInputChange}
                                                placeholder="VM Core Count Bucket"
                                            />
                                        </div>
                                        </div>
                                        <div className="grid grid-rows-3 w-full h-full items-center justify-center">
                                            <div className="w-full h-full flex justify-center items-center">
                                                VM Deleted
                                            </div>
                                            <div className="w-full h-full flex justify-center items-center row-span-2">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="vmdeleted"
                                                id="Type"
                                                type="text"
                                                value={vmdeleted}
                                                onChange={handleInputChange}
                                                placeholder="VM Deleted"
                                            />
                                        </div>
                                        </div>
                                    </div>
                            </div>
                            <div className="w-full h-full bg-transparent row-span-1 rounded-b-3xl flex justify-end">
                                    <button type="submit" className="hover:shadow-lg hover:shadow-lime-500/50 hover:bg-lime-300 duration-1000 w-32 flex items-center justify-center h-18 rounded-br-3xl">Calculate<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-6 h-6 ml-2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 15.75V18m-7.5-6.75h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V13.5Zm0 2.25h.008v.008H8.25v-.008Zm0 2.25h.008v.008H8.25V18Zm2.498-6.75h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V13.5Zm0 2.25h.007v.008h-.007v-.008Zm0 2.25h.007v.008h-.007V18Zm2.504-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5Zm0 2.25h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V18Zm2.498-6.75h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V13.5ZM8.25 6h7.5v2.25h-7.5V6ZM12 2.25c-1.892 0-3.758.11-5.593.322C5.307 2.7 4.5 3.65 4.5 4.757V19.5a2.25 2.25 0 0 0 2.25 2.25h10.5a2.25 2.25 0 0 0 2.25-2.25V4.757c0-1.108-.806-2.057-1.907-2.185A48.507 48.507 0 0 0 12 2.25Z" />
</svg>

</button>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div className="col-span-2 grid gap-4 grid-rows-2 w-full h-full rounded-3xl">
                        <div className="grid gap-4 grid-cols-2 w-full h-full rounded-3xl">
                            <div className="centerlayer bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl grid grid-rows-5">
                                <div className="w-full h-full row-span-1 rounded-3xl flex justify-center items-center">
                                    <h className="text-2xl tracking-widest font-normal bg-black text-white px-4 rounded-xl h-8" style={style}>Available Vendors</h>
                                <style>
                                {`
              @keyframes animate {
                0% {
                  background-position: 400%;
                }
                100% {
                  background-position: 0%;
                }
              }
            `}
                            </style>
                                </div>
                                <div className="w-full h-full row-span-4 rounded-3xl flex justify-center items-center">
                                    {holder?(<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-56 h-56 text-gray-400 animate-pulse">
  <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15a4.5 4.5 0 0 0 4.5 4.5H18a3.75 3.75 0 0 0 1.332-7.257 3 3 0 0 0-3.758-3.848 5.25 5.25 0 0 0-10.233 2.33A4.502 4.502 0 0 0 2.25 15Z" />
                                    </svg>
                                        ):(
                                            <div className="w-full h-56 px-4 pt-4 overflow-y-auto">{loader?(<div className="rounded-md p-4 max-w-sm w-full mx-auto h-full">
  <div className="animate-pulse flex space-x-4 w-full h-full">
    <div className="rounded-full bg-slate-700 h-10 w-10"></div>
    <div className="flex-1 space-y-6 py-1">
      <div className="h-2 bg-slate-700 rounded"></div>
      <div className="space-y-3">
        <div className="grid grid-cols-3 gap-4">
          <div className="h-2 bg-slate-700 rounded col-span-2"></div>
          <div className="h-2 bg-slate-700 rounded col-span-1"></div>
        </div>
        <div className="h-2 bg-slate-700 rounded"></div>
      </div>
    </div>
  </div>
</div>):(<div className="w-full h-full">
                                        <div className="w-full flex items-center justify-center">Microsoft Azure</div>
                                        {Object.keys(azure_info).length > 0 ? (
        <div className="w-full h-[425px]">
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Name:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Name}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">API Name:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.API_Name}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Instance Memory:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Instance_Memory}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">vCPUs:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.vCPUs}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">GiB of Memory per vCPU:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.GiB_of_Memory_per_vCPU}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
             <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">GPUs:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.GPUs}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Instance Storage:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Instance_Storage}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">On Demand Cost:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.On_Demand}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Linux Reserved Cost:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Linux_Reserved_cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Windows Reserved Cost:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Windows_Reserved_Cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Windows Spot Cost:</div>
                <div className="w-full h-full text-right"> {azure_info.Microsoft_Azure.Windows_Spot_Cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
        </div>
    ) : (
        <div className="w-full flex py-4 justify-center">No data found for the given criteria.</div>
    )}
                                                    <div className="w-full flex items-center justify-center">Amazon EC2</div>
                                                    {Object.keys(aws_ec2_info).length > 0 ? (
        <div className="w-full h-full">
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Name:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Name}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">API Name:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.API_Name}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Instance Memory:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Instance_Memory}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">vCPUs:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.vCPUs}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">GiB of Memory per vCPU:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.GiB_of_Memory_per_vCPU}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
             <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">GPUs:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.GPUs}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Instance Storage:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Instance_Storage}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">On Demand Cost:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.On_Demand}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Linux Reserved Cost:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Linux_Reserved_cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Windows Reserved Cost:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Windows_Reserved_Cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
            <div className="w-full h-8 grid-cols-2 grid">
                <div className="w-full h-full">Windows Spot Cost:</div>
                <div className="w-full h-full text-right"> {aws_ec2_info.Amazon_EC2.Windows_Spot_Cost}</div>
            </div>
            <div className="lineseg  h-1 bg-gray-400 rounded-full"></div>
        </div>
    ) : (
        <div className="w-full flex py-4 justify-center">No data found for the given criteria.</div>
    )}
</div>
)}</div>

)}
                                </div>
                            </div>
                            <div className="rtcontainer bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl grid grid-rows-5">
                                <div className="w-full h-full row-span-1 rounded-3xl flex justify-center items-center">
                                    <h className="text-2xl tracking-widest font-normal bg-black text-white px-4 rounded-xl h-8" style={style}>Predicted Results</h>
                                <style>
                                {`
              @keyframes animate {
                0% {
                  background-position: 400%;
                }
                100% {
                  background-position: 0%;
                }
              }
            `}
                            </style>
                                </div>
                                <div className="w-full h-full row-span-4 rounded-3xl flex justify-center items-center">
                                    {holder?(<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" className="w-56 h-56 text-gray-400 animate-pulse">
  <path stroke-linecap="round" stroke-linejoin="round" d="M9 3.75H6.912a2.25 2.25 0 0 0-2.15 1.588L2.35 13.177a2.25 2.25 0 0 0-.1.661V18a2.25 2.25 0 0 0 2.25 2.25h15A2.25 2.25 0 0 0 21.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 0 0-2.15-1.588H15M2.25 13.5h3.86a2.25 2.25 0 0 1 2.012 1.244l.256.512a2.25 2.25 0 0 0 2.013 1.244h3.218a2.25 2.25 0 0 0 2.013-1.244l.256-.512a2.25 2.25 0 0 1 2.013-1.244h3.859M12 3v8.25m0 0-3-3m3 3 3-3" />
</svg>
                                        ):(
                                            <div className="w-full h-56 px-4 pt-4">{loader?(<div className="rounded-md p-4 max-w-sm w-full mx-auto h-full">
  <div className="animate-pulse flex space-x-4 w-full h-full">
    <div className="rounded-full bg-slate-700 h-10 w-10"></div>
    <div className="flex-1 space-y-6 py-1">
      <div className="h-2 bg-slate-700 rounded"></div>
      <div className="space-y-3">
        <div className="grid grid-cols-3 gap-4">
          <div className="h-2 bg-slate-700 rounded col-span-2"></div>
          <div className="h-2 bg-slate-700 rounded col-span-1"></div>
        </div>
        <div className="h-2 bg-slate-700 rounded"></div>
      </div>
    </div>
  </div>
</div>):(<div className="w-full h-full grid-rows-3 grid">
                                        <div className="w-full h-full flex items-center justify-center">
                                            <h1>On demand monthly cost</h1>
                                        </div>
                                                <div className="w-full h-full flex items-center justify-center text-green-400">
                                            <h1 className="font-normal text-4xl overflow-x-hidden">${parseFloat(prediction * 720).toFixed(2)}
                                            <div className={"h-1 rounded-full  bg-green-400"+(loader ? "" : " move")}></div>
                                            </h1>
                                        </div>
                                        <div className="w-full h-full flex items-center justify-center">
                                            {autoscale?(<h1>Autoscaling is required</h1>):(<h1>Autoscaling is not required</h1>)}
                                        </div>
                                    </div>)}</div>

)}
                                </div>
                            </div>
                        </div>
                        <div className="bcontainer grid grid-rows-5 bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl">
                            <div className="row-span-1 w-full h-full rounded-3xl flex items-center justify-center">
                            <h className="text-2xl tracking-widest font-normal bg-black text-white px-4 rounded-xl h-8" style={style}>Comparative Analysis</h>
                                <style>
                                {`
              @keyframes animate {
                0% {
                  background-position: 400%;
                }
                100% {
                  background-position: 0%;
                }
              }
            `}
                            </style>
                            </div>
                            <div className="row-span-4 w-full h-full px-4 rounded-b-3xl">
                                <div className="w-full h-full flex items-center justify-center">
                                    <LineChart width={900} height={250} data={data}
                                      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                      <CartesianGrid strokeDasharray="3 3" />
                                      <XAxis dataKey="name" />
                                      <YAxis />
                                      <Tooltip />
                                      <Legend />
                                      <Line type="monotone" dataKey="Predicted_Cost" stroke="#8884d8" />
                                      <Line type="monotone" dataKey="Microsoft_Azure_Cost" stroke="#02d448" />
                                      <Line type="monotone" dataKey="Amazon_EC2" stroke="#4287f5" />
                                    </LineChart>

                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="blob w-[800px] h-[800px] rounded-full absolute bottom-0 right-0 -z-10 bg-gradient-to-r from-indigo-200 via-purple-200 to-pink-200 blur-2xl bg-opacity-50"></div>
            <div className="blob w-[1000px] h-[1000px] rounded-full absolute bottom-0 left-0 -z-10 bg-gradient-to-r from-red-200 via-gray-100 to-blue-100 blur-2xl bg-opacity-50"></div>
            <div className="blob w-[600px] h-[600px] rounded-full absolute bottom-0 left-0 -z-10 bg-gradient-to-r from-slate-100 via-teal-100 to-blue-100 blur-2xl bg-opacity-50"></div>
            <div className="blob w-[300px] h-[300px] rounded-full absolute bottom-0 left-0 -z-10 bg-gradient-to-r from-green-200 via-cyan-200 to-Fuchsia-300 blur-2xl bg-opacity-50"></div>
        </div>
    );
}
