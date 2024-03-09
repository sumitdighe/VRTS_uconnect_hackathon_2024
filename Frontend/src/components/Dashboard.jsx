import React, { useEffect,useRef,useState } from 'react';
import { Link } from 'react-router-dom';
import { PieChart, Pie, Cell ,Sector} from 'recharts';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { gsap } from 'gsap/all';
import axios from "axios";

export default function Dashboard() {
const data = [
  {
    name: '0',
    Microsoft_Azure_Cost: 40000,
    On_premises_Cost: 24000,
    amt: 24000,
  },
  {
    name: '1 Year',
    Microsoft_Azure_Cost: 30000,
    On_premises_Cost: 13980,
    amt: 22100,
  },
  {
    name: '2 Year',
    Microsoft_Azure_Cost: 20000,
    On_premises_Cost: 98000,
    amt: 22900,
  },
  {
    name: '3 Year',
    Microsoft_Azure_Cost: 27800,
    On_premises_Cost: 39080,
    amt: 20000,
  },
  {
    name: '4 Year',
    Microsoft_Azure_Cost: 18900,
    On_premises_Cost: 48000,
    amt: 21810,
  },
  {
    name: '5 Year',
    Microsoft_Azure_Cost: 23900,
    On_premises_Cost: 38000,
    amt: 25000,
  },
];


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
  }, []);

  const [instance_memory, setinstance_memory] = useState('0');
    const [vcpus, setvcpus] = useState('0');
    const [avgcpu_usage, setavgcpu_usage] = useState('0');
    const [vmmemorybucket, setvmmemorybucket] = useState('0');
    const [prediction, setPrediction] = useState(null);

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

    const handleInput1Change = (event) => {
        setinstance_memory(event.target.value);
    }

    const handleInput2Change = (event) => {
        setvcpus(event.target.value);
    }
    const handleInput3Change = (event) => {
        setavgcpu_usage(event.target.value);
    }
    const handleInput4Change = (event) => {
        setvmmemorybucket(event.target.value);
    }
    // const handleInput5Change = (event) => {
    //     setinstance_memory(event.target.value);
    // }


const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response =
                await axios.post('http://localhost:8000/MainApp/sample/',
                // await axios.post('http://43.204.220.52/MainApp/sample/',
                    {
                instance_memory: instance_memory,
                vcpus: vcpus,
                        avgcpu_usage: avgcpu_usage,
                vmmemorybucket: vmmemorybucket
            });
            setPrediction(response.data.message);
        } catch (error) {
            console.error('Error:', error);
        }
    }
    const style = {
        background: 'linear-gradient(90deg,#808080,#808080,#808080, #fcfffd, #808080,#808080,#808080,#fcfffd, #808080,#808080,#808080,#fcfffd,#808080,#808080,#808080)',
        backgroundSize: '400%',
        WebkitTextFillColor: 'transparent',
        WebkitBackgroundClip: 'text',
        animation: 'animate 25s linear infinite'
    };
    return (
        <div className="flex flex-col h-screen">
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
            {/*<div className="grid grid-cols-3 w-full h-20">*/}
            {/*    <div className="w-full h-full pl-8 flex items-center">*/}
            {/*        <Link>*/}
            {/*            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">*/}
            {/*                <path stroke-linecap="round" stroke-linejoin="round" d="M9 15L3 9m0 0l6-6M3 9h12a6 6 0 010 12h-3" />*/}
            {/*            </svg>*/}
            {/*        </Link>*/}
            {/*    </div>*/}
            {/*    <div className="w-full h-full flex items-center justify-center relative">*/}
            {/*        <form className="relative">*/}
            {/*            <input*/}
            {/*                className="py-2 pl-4 w-96 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"*/}
            {/*                type="text"*/}
            {/*                placeholder="Search"*/}
            {/*            />*/}
            {/*            <button*/}
            {/*                className="bg-teal-400 duration-1000 hover:bg-teal-500 hover:shadow-lg hover:shadow-teal-500/50 absolute right-1 top-1 h-10 rounded-full w-16 flex items-center justify-center"*/}
            {/*                type="submit"*/}
            {/*            >*/}
            {/*                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">*/}
            {/*                    <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />*/}
            {/*                </svg>*/}

            {/*            </button>*/}
            {/*        </form>*/}
            {/*    </div>*/}
            {/*    <div className="w-full h-full flex items-center justify-end pr-8">*/}
            {/*        <select*/}
            {/*            className="h-12 px-4 border-solid border-white rounded-3xl bg-transparent w-32 border-0 focus:outline-none"*/}
            {/*            name="year"*/}
            {/*            id="year"*/}
            {/*        >*/}
            {/*            <option value="2022">AZURE</option>*/}
            {/*            <option value="2023">AWS</option>*/}
            {/*            <option value="2024">GCP</option>*/}
            {/*        </select>*/}
            {/*    </div>*/}
            {/*</div>*/}
            <div className="flex-1 w-full px-4 py-4">
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
                                    <div className="grid grid-rows-3 w-full h-full">
                                        <div className="w-full h-full flex items-center justify-center">
                                            <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                                value={instance_memory} onChange={handleInput1Change}
                                            >
                                                {options.map((option, index) => (
                                                    <option key={index} value={option}>{option} GiB</option>
                                                ))}
                                            </select>
                                        </div>
                                        <div className="w-full h-full flex items-center justify-center">
                                           <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                                value={vcpus} onChange={handleInput2Change}
                                            >
                                                {options2.map((options2, index) => (
                                                    <option key={index} value={options2}>{options2} vCPUs</option>
                                                ))}
                                            </select>
                                        </div>
                                        <div className="w-full h-full flex items-center justify-center">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                                type="text"
                                                value={avgcpu_usage}
                                                onChange={handleInput3Change}
                                                placeholder="Average CPU Usage"
                                            />
                                        </div>
                                    </div>
                                    <div className="grid grid-rows-3 w-full h-full">
                                        <div className="w-full h-full flex items-center justify-center">

                                        <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                            >
                                                <option value="2022">Low Budget</option>
                                                <option value="2023">Medium Budget</option>
                                                <option value="2024">High Budget</option>
                                                <option value="2024">Very High Budget</option>
                                            </select>
                                        </div>
                                        <div className="w-full h-full flex items-center justify-center">
                                            <select
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                            >
                                                <option value="2022">Instance Storage</option>
                                                <option value="2023">HDD</option>
                                                <option value="2024">SDD</option>
                                            </select>
                                        </div>
                                        <div className="w-full h-full flex items-center justify-center">
                                            <input
                                                className="py-2 pl-4 w-56 h-12 rounded-3xl border-solid border-2 border-gray-400 focus:outline-none bg-transparent"
                                                name="Property Type"
                                                id="Type"
                                                type="text"
                                                value={vmmemorybucket}
                                                onChange={handleInput4Change}
                                                placeholder="VM Memory Bucket"
                                            />
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
                                <div className="w-full h-full row-span-1 rounded-3xl flex justify-center items-center"><h className="text-xl tracking-widest bg-black text-white px-4 rounded-xl h-8">Total on-premises over 5 year(s)</h></div>
                                <div className="w-full h-full row-span-4 rounded-3xl flex justify-center items-center">



                                </div>
                            </div>
                            <div className="rtcontainer bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl grid grid-rows-5">
                                <div className="w-full h-full row-span-1 rounded-3xl flex justify-center items-center"><h className="text-xl tracking-widest bg-black text-white px-4 rounded-xl h-8">Total Azure cost over 5 year(s)</h></div>
                                <div className="w-full h-full row-span-4 rounded-3xl flex justify-center items-center">

                                </div>
                            </div>
                        </div>
                        <div className="bcontainer grid grid-rows-5 bg-white backdrop-blur-md bg-blur-md bg-opacity-30 border-solid border-white border-t-2 border-l-2 w-full h-full rounded-3xl">
                            <div className="row-span-1 w-full h-full rounded-3xl flex items-center justify-center">
                                <h className="text-xl tracking-widest bg-black text-white px-4 rounded-xl h-8">{prediction}</h>
                            </div>
                            <div className="row-span-4 w-full h-full px-4 rounded-b-3xl">
                                <div className="w-full h-52 rounded-b-3xl overflow-y-auto">
                                    <LineChart width={900} height={200} data={data}
                                      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                                      <CartesianGrid strokeDasharray="3 3" />
                                      <XAxis dataKey="name" />
                                      <YAxis />
                                      <Tooltip />
                                      <Legend />
                                      <Line type="monotone" dataKey="On_premises_Cost" stroke="#8884d8" />
                                      <Line type="monotone" dataKey="Microsoft_Azure_Cost" stroke="#82ca9d" />
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
