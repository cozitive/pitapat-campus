import React, { ChangeEvent, Dispatch, SetStateAction, useCallback, useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { selectCollege } from "../../store/slices/college";
import { selectMajor } from "../../store/slices/major";
import { College, Gender, Major } from "../../types";
import CompleteSentence from "./CompleteSentence";


interface IProps {
  nickname: string,
  setNickname: Dispatch<SetStateAction<string>>,
  birthday: Date | null,
  setBirthday: Dispatch<SetStateAction<Date | null>>,
  college: College | null,
  setCollege: Dispatch<SetStateAction<College | null>>,
  major: Major | null,
  setMajor: Dispatch<SetStateAction<Major | null>>,
  gender: Gender,
  setGender: Dispatch<SetStateAction<Gender>>,
  targetGender: Gender,
  setTargetGender: Dispatch<SetStateAction<Gender>>,
  setStep: Dispatch<SetStateAction<number>>,
}

export default function PersonalInformation({
  nickname,
  setNickname,
  birthday,
  setBirthday,
  college,
  setCollege,
  major,
  setMajor,
  gender,
  setGender,
  targetGender,
  setTargetGender,
  setStep,
}: IProps) {
  const colleges = useSelector(selectCollege).colleges;
  const majors = useSelector(selectMajor).majors;
  const [targetMajors, setTargetMajors] = useState<Major[]>([]);
  const [hasSubmit, setHasSubmit] = useState<boolean>(false);

  const changeBirthdayHandler = (event: string) => {
    if (event.match(/^(19[0-9][0-9]|20\d{2})-(0[0-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$/)) {
      setBirthday(new Date(event));
    }
  };

  const changeCollegeHandler = useCallback((event: ChangeEvent<HTMLSelectElement>) => {
    const targetCollege = colleges.find((col) => (col.name === event.target.value));
    setCollege((targetCollege) ? targetCollege : null);
  }, [setCollege, colleges]);

  const changeMajorHandler = useCallback((event: ChangeEvent<HTMLSelectElement>) => {
    const targetMajor = majors.find((mjr) => (mjr.name === event.target.value));
    setMajor((targetMajor) ? targetMajor : null);
  }, [setMajor, majors]);

  const changeGenderHandler = useCallback((event: ChangeEvent<HTMLSelectElement>) => {
    setGender((event.target.value === "M") ? (Gender.MALE) : (Gender.FEMALE));
  }, [setGender]);

  const changeTargetGenderHandler = useCallback((event: ChangeEvent<HTMLSelectElement>) => {
    setTargetGender((event.target.value === "M") ? (Gender.MALE) : ((event.target.value === "F") ? (Gender.FEMALE) : (Gender.ALL)));
  }, [setTargetGender]);

  const clickConfirmHandler = useCallback(() => {
    if (nickname && birthday && college && major && gender && targetGender) {
      setStep(3);
    }
    else {
      setHasSubmit(true);
    }
  }, [setStep, nickname, birthday, college, major, gender, targetGender]);

  useEffect(() => {
    if (college) {
      const collegeMajors = majors.filter((mjr) => (college.majors.includes(mjr.key)));
      setTargetMajors(collegeMajors);
    }
    else {
      setTargetMajors([]);
    }
  }, [college, majors]);

  return (
    < section className={"h-screen w-full flex flex-col mt-12 mb-16"} >
      <CompleteSentence />
      <article className={"mt-4 ml-8 leading-10"}>닉네임</article>
      <div className="text-center">
        <input className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          placeholder={"닉네임"}
          value={nickname}
          onChange={(event) => setNickname(event.target.value)}>
        </input>
      </div>
      <div>
        <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !nickname) ? "필수 작성 항목입니다." : " "}</article>
        <article className={(hasSubmit && !nickname) ? "ml-8 leading-10" : "mt-4 ml-8 leading-10"}>생년월일</article>
      </div>
      <div className="text-center">
        <input className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          placeholder={"YYYY-MM-DD"}
          onChange={(event) => changeBirthdayHandler(event.target.value)}>
        </input>
      </div>
      <div>
        <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !birthday) ? "필수 작성 항목입니다." : " "}</article>
        <article className={(hasSubmit && !birthday) ? "ml-8 leading-10" : "mt-4 ml-8 leading-10"}>단과대</article>
      </div>
      <div className="text-center">
        <select
          className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          value={undefined}
          onChange={changeCollegeHandler}
        >{
            ([{ key: 0, name: "", majors: [] }] as College[])
              .concat(colleges)
              .map((col) => (
                <option
                  key={col.key}
                  value={col.name}
                >{
                    col.name
                  }
                </option>
              ))
          }</select>
      </div>
      <div>
        <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !college) ? "필수 작성 항목입니다." : " "}</article>
        <article className={(hasSubmit && !college) ? "ml-8 leading-10" : "mt-4 ml-8 leading-10"}>학과</article>
      </div>
      <div className="text-center">
        <select
          className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          value={undefined}
          onChange={changeMajorHandler}
        >{
            targetMajors.map((mjr) => (
              <option
                key={mjr.key}
                value={mjr.name}
              >{
                  mjr.name
                }
              </option>
            ))
          }</select>
      </div>
      <div>
        <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !major) ? "필수 작성 항목입니다." : " "}</article>
        <article className={(hasSubmit && !major) ? "ml-8 leading-10" : "mt-4 ml-8 leading-10"}>성별</article>
      </div>
      <div className="text-center">
        <select
          className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          value={gender}
          onChange={changeGenderHandler}
        >
          <option key="0" value={Gender.MALE}>남자</option>
          <option key="1" value={Gender.FEMALE}>여자</option>
        </select>
      </div>
      <div>
        <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !gender) ? "필수 작성 항목입니다." : " "}</article>
        <article className={(hasSubmit && !gender) ? "ml-8 leading-10" : "mt-4 ml-8 leading-10"}>관심성별</article>
      </div>
      <div className="text-center">
        <select
          className={"w-64 indent-4 border-solid border-b-4 border-l-2 border-r-2 rounded-md"}
          value={targetGender}
          onChange={changeTargetGenderHandler}
        >
          <option key="0" value={Gender.FEMALE}>여자</option>
          <option key="1" value={Gender.MALE}>남자</option>
          <option key="2" value={Gender.ALL}>모두</option>
        </select>
      </div>
      <article className={"ml-8 text-red-500 text-sm"}>{(hasSubmit && !targetGender) ? "필수 작성 항목입니다." : " "}</article>
      <div className={"text-center"}>
        <button
          className={"bg-pink-500 text-center text-white mt-8 w-36 h-12 rounded-md"}
          onClick={() => clickConfirmHandler()}
        >
          다음
        </button>
      </div>
    </section >
  );
}