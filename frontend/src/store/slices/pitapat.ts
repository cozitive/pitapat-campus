import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Pitapat } from "../../types";
import DummyData from "../../DummyData";
import { RootState } from "../index";


const storeKey = "pitapat";

const getInitialState = (): Pitapat[] => {
  let savedValue = localStorage.getItem(storeKey);
  if (savedValue === null) {
    localStorage.setItem(storeKey, JSON.stringify(DummyData.pitapats));
    savedValue = localStorage.getItem(storeKey);
  }
  return JSON.parse(savedValue!) as Pitapat[];
};

const pitapatSlice = createSlice({
  name: "pitapat",
  initialState: { pitapats: getInitialState() },
  reducers: {
    add: (state, action: PayloadAction<Pitapat>) => {
      const newPitapats = [...state.pitapats, action.payload];
      localStorage.setItem(storeKey, JSON.stringify(newPitapats));
      state.pitapats = newPitapats;
    },
    delete: (state, action: PayloadAction<Pitapat>) => {
      const newPitapats = state.pitapats.filter((p) => (p.from !== action.payload.from) && (p.to !== action.payload.to))
      localStorage.setItem(storeKey, JSON.stringify(newPitapats));
      state.pitapats = newPitapats;
    },
  },
})

export const selectPitapat = (state: RootState) => state.pitapat;
const pitapatReducer = pitapatSlice.reducer;
export default pitapatReducer;