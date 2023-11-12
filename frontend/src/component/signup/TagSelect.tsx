import React, { Dispatch, SetStateAction, useCallback, useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import { FormControl, InputLabel, MenuItem, Select } from "@mui/material";
import { pink } from "@mui/material/colors";
import TagElement from "./TagElement";
import style from "../../constant/style";
import { AppDispatch } from "../../store";
import { getTags, selectTag } from "../../store/slices/tag";
import { Tag } from "../../types";


export interface IProps {
  tags: Tag[];
  setTags: Dispatch<SetStateAction<Tag[]>>;
  setStep: Dispatch<SetStateAction<number>>;
}

export default function TagSelect({
  tags,
  setTags,
  setStep,
}: IProps) {
  const dispatch = useDispatch<AppDispatch>();
  const loadedTags = useSelector(selectTag).tags;
  const [selectedTag, setSelectedTag] = useState<Tag>();
  const [selectedTagKey, setSelectedTagKey] = useState<number>(-1);
  const [submittedWithNoTag, setSubmittedWithNoTag] = useState<boolean>(false);
  const [isTagLoaded, setIsTagLoaded] = useState<boolean>(false);

  useEffect(() => {
    if ((selectedTagKey < 1) && isTagLoaded) {
      return;
    }
    let targetTag = loadedTags.find((t) => (t.key === selectedTagKey));
    if (!targetTag) {
      dispatch(getTags());
      targetTag = loadedTags.find((t) => (t.key === selectedTagKey));
      setIsTagLoaded(true);
    }
    setSelectedTag(targetTag);
  }, [loadedTags, selectedTagKey, dispatch, isTagLoaded]);

  const addTagOnClick = useCallback(() => {
    if (selectedTag) {
      if (!tags.includes(selectedTag)) {
        setTags([...tags, selectedTag]);
      }
    }
  }, [selectedTag, tags, setTags]);

  const deleteTag = useCallback((tagKey: number) => {
    const newTags = tags.filter((t) => t.key !== tagKey);
    setTags(newTags);
  }, [tags, setTags]);

  const confirmOnClick = useCallback(() => {
    if (tags.length !== 0) {
      setStep(4);
    }
    else {
      setSubmittedWithNoTag(true);
    }
  }, [setStep, tags]);

  const backOnClick = useCallback(() => {
    setTags([]);
    setStep(2);
  }, [setTags, setStep]);
  return (
    <section className={style.page.base}>
      <p className={style.component.signIn.notification}>
        나를 표현하는 태그를 입력해보세요!<br/>
        ex) 취미 (등산, 그림, ...)
      </p>
      <section className={"w-full flex-1 flex flex-col items-center"}>
        <div className={"flex flex-row justify-center mt-8"}>
          <article className={"flex flex-col item-center"}>
            <FormControl
              sx={{
                maxWidth: 320,
                minWidth: 240,
              }}
              size={"small"}
              required
            >
              <InputLabel>
                {"태그"}
              </InputLabel>
              <Select
                label={"태그"}
                variant={"outlined"}
                value={selectedTagKey}
                onChange={(e) => {
                  setSelectedTagKey(parseInt(`${e.target.value}`));
                }}
              >
                {
                  loadedTags
                    .map((t) => ({ name: t.name, value: t.key }))
                    .map(({ name, value }) => (<MenuItem value={value} key={value}>{name}</MenuItem>))
                }
              </Select>
            </FormControl>
          </article>
          <button
            className={"ml-2"}
            onClick={addTagOnClick}
          >
            <AddCircleIcon
              style={{ color: pink[500] }}
              fontSize={"large"}
            />
          </button>
        </div>
        <article
          className={"ml-2 text-red-500 mb-4 text-sm"}
        >
          {
            (submittedWithNoTag) ?
              "최소한 한 개의 태그가 있어야 해요." :
              null
          }
        </article>
        <article
          className={"w-4/5 max-w-xs flex flex-row flex-wrap text-base font-bold justify-start"}
        >
          {
            tags.map((tag) => (
              <TagElement
                key={tag.key}
                name={tag.name}
                onDelete={() => { deleteTag(tag.key); }}
              />
            ))
          }
        </article>
      </section>
      <section className={style.component.signIn.buttonWrapper}>
        <button
          className={`${style.button.base} ${style.button.colorSet.secondary} mb-2`}
          onClick={backOnClick}
        >
          뒤로 가기
        </button>
        <button
          className={`${style.button.base} ${style.button.colorSet.main}`}
          onClick={confirmOnClick}
        >
          다음
        </button>
      </section>
    </section>
  );
}
