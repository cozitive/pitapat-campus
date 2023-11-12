import React, { useCallback, useEffect, useState } from "react";
import { useDispatch , useSelector } from "react-redux";
import { pink } from "@mui/material/colors";
import Slider from "@mui/material/Slider";
import UserFilterElement from "./UserFilterElement";
import style from "../constant/style";
import { AppDispatch } from "../store";
import { getColleges, selectCollege } from "../store/slices/college";
import { getMajorsByUniversity, selectMajor } from "../store/slices/major";
import { getTags, selectTag } from "../store/slices/tag";
import { getNewUsers, selectUser, userActions } from "../store/slices/user";
import { College, Major, Tag } from "../types";


interface IProps {
  onModalClose: () => void;
}

export default function UserFilter({
  onModalClose,
}: IProps) {
  const dispatch = useDispatch<AppDispatch>();
  const loginUser = useSelector(selectUser).loginUser;
  const colleges = useSelector(selectCollege).colleges;
  const majors = useSelector(selectMajor).majors;
  const tags = useSelector(selectTag).tags;
  const filter = useSelector(selectUser).filter;
  const [college, setCollege] = useState<number | "">("");
  const [major, setMajor] = useState<number | "">("");
  const [tag, setTag] = useState<number | "">("");
  const [includedColleges, setIncludedColleges] = useState<College[]>([]);
  const [excludedColleges, setExcludedColleges] = useState<College[]>([]);
  const [includedMajors, setIncludedMajors] = useState<Major[]>([]);
  const [excludedMajors, setExcludedMajors] = useState<Major[]>([]);
  const [includedTags, setIncludedTags] = useState<Tag[]>([]);
  const [excludedTags, setExcludedTags] = useState<Tag[]>([]);
  const [ageRange, setAgeRange] = useState<number[]>([filter?.minAge ?? 19, filter?.maxAge ?? 30]);

  useEffect(() => {
    const includedColleges = filter?.includedColleges;
    const excludedColleges = filter?.excludedColleges;
    if (includedColleges) {
      setIncludedColleges(colleges.filter((c) => includedColleges.indexOf(c.key) >= 0 ));
    }
    if (excludedColleges) {
      setExcludedColleges(colleges.filter((c) => excludedColleges.indexOf(c.key) >= 0 ));
    }
  }, [filter, colleges, setIncludedColleges, setExcludedColleges]);

  useEffect(() => {
    const includedMajors = filter?.includedMajors;
    const excludedMajors = filter?.excludedMajors;
    if (includedMajors) {
      setIncludedMajors(majors.filter((m) => includedMajors.indexOf(m.key) >= 0 ));
    }
    if (excludedMajors) {
      setExcludedMajors(majors.filter((m) => excludedMajors.indexOf(m.key) >= 0 ));
    }
  }, [filter, majors, setIncludedMajors, setExcludedMajors]);

  useEffect(() => {
    const includedTags = filter?.includedTags;
    const excludedTags = filter?.excludedTags;
    if (includedTags) {
      setIncludedTags(tags.filter((t) => includedTags.indexOf(t.key) >= 0 ));
    }
    if (excludedTags) {
      setExcludedTags(tags.filter((t) => excludedTags.indexOf(t.key) >= 0 ));
    }
  }, [filter, tags, setIncludedTags, setExcludedTags]);

  useEffect(() => {
    if (!loginUser) {
      return;
    }
    const university = loginUser.university;
    if (university && colleges.length === 0) {
      dispatch(getColleges(university));
    }
  }, [dispatch, loginUser, colleges]);

  useEffect(() => {
    if (!loginUser) {
      return;
    }
    const university = loginUser.university;
    if (university && majors.length === 0) {
      dispatch(getMajorsByUniversity(university));
    }
  }, [dispatch, loginUser, majors]);

  useEffect(() => {
    if (tags.length === 0) {
      dispatch(getTags());
    }
  }, [dispatch, tags]);

  const onAgeChange = useCallback((_: Event, newValue: number | number[]) => {
    setAgeRange(newValue as number[]);
  }, [setAgeRange]);

  const onClickApply = useCallback(async () => {
    if (!loginUser) {
      return;
    }
    const filter = {
      pageIndex: 1,
      gender: loginUser.interestedGender,
      minAge: ageRange[0],
      maxAge: ageRange[1],
      includedColleges: includedColleges.map((c) => c.key),
      excludedColleges: excludedColleges.map((c) => c.key),
      includedMajors: includedMajors.map((m) => m.key),
      excludedMajors: excludedMajors.map((m) => m.key),
      includedTags: includedTags.map((t) => t.key),
      excludedTags: excludedTags.map((t) => t.key),
    };
    dispatch(userActions.setFilter(filter));
    dispatch(getNewUsers(filter));
    onModalClose();
  }, [
    loginUser,
    ageRange,
    includedColleges,
    excludedColleges,
    includedMajors,
    excludedMajors,
    includedTags,
    excludedTags,
    onModalClose,
    dispatch,
  ]);

  return (
    <section className={"h-fit w-fit flex flex-col items-center bg-white p-4"}>
      <section>
        <div className={"flex flex-row"}>
          <p className={"text-left pr-1"}>나이</p>
          <p className={"text-gray-500"}>({ageRange[0]}~{ageRange[1] < 30 ? ageRange[1] : "30+"})</p>
        </div>
        <div className="flex flex-col items-center mb-4">
          <Slider
            value={ageRange}
            onChange={onAgeChange}
            min={19}
            max={30}
            style={{ color: pink[400] }}
            sx={{
              maxWidth: 300,
              minWidth: 300,
            }}
          />
        </div>
        <UserFilterElement<College>
          title="단과대"
          value={college}
          values={colleges}
          includedValues={includedColleges}
          excludedValues={excludedColleges}
          setValue={setCollege}
          setIncludedValues={setIncludedColleges}
          setExcludedValues={setExcludedColleges}
        />
        <UserFilterElement<Major>
          title="학과"
          value={major}
          values={majors}
          includedValues={includedMajors}
          excludedValues={excludedMajors}
          setValue={setMajor}
          setIncludedValues={setIncludedMajors}
          setExcludedValues={setExcludedMajors}
        />
        <UserFilterElement<Tag>
          title="태그"
          value={tag}
          values={tags}
          includedValues={includedTags}
          excludedValues={excludedTags}
          setValue={setTag}
          setIncludedValues={setIncludedTags}
          setExcludedValues={setExcludedTags}
        />
      </section>
      <button
        className={`${style.button.base} ${style.button.colorSet.main} mt-2`}
        onClick={onClickApply}
      >
        적용
      </button>
    </section>
  );
}
